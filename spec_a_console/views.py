from django.shortcuts import redirect, render, get_object_or_404, reverse  # noqa: F401, E501, # type: ignore
from django.contrib.auth.decorators import login_required
from django.views import generic  # type: ignore
from django.utils.text import slugify
# from django.http import HttpResponse
from django.http import Http404
from django.contrib import messages  # type: ignore
from .models import ConsoleSystem
from .forms import SystemReviewForm


# Create your views here.
# def index(request):
#     return HttpResponse("Hello, this is the spec_a_console index page.")


class ConsoleSystemListView(generic.ListView):
    """A view to list all approved ConsoleSystem instances."""
    model = ConsoleSystem
    template_name = 'spec_a_console/index.html'
    context_object_name = 'console_systems'
    paginate_by = 10
    queryset = ConsoleSystem.objects.filter(
        approval=1).order_by('-created_on')


def console_system_detailed_view(request, slug):
    """A view to show details of a specific ConsoleSystem."""
    # queryset = ConsoleSystem.objects.filter(approval=1)
    # system = get_object_or_404(queryset, slug=slug)

    system = get_object_or_404(ConsoleSystem, slug=slug)

    # Only show unapproved systems to their creator
    if system.approval != 1 and system.created_by != request.user:
        raise Http404("No ConsoleSystem matches the given query.")

    if system.approval != 1 and system.created_by == request.user:
        messages.info(request, "This system is awaiting approval.")

    # TODO: add reviews of the system here
    reviews = system.reviews.filter().order_by('-created_on')
    review_count = system.reviews.filter(approved=True).count()

    if request.method == "POST":
        review_form = SystemReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)  # get form ref w/out sav
            review.reviewer = request.user  # finsih populating form
            review.system = system  # get ref to post comment is being put on
            review.save()  # now time to save
            # Below: send message to user confirming submission
            messages.add_message(request, messages.SUCCESS,
                                 'Review submitted and awaiting approval')
            # Redirect to the same page to prevent resubmission
            return redirect('system_detail', slug=system.slug)

    # Create a new form, so user can add another review if they wish
    review_form = SystemReviewForm()

    return render(
        request,
        'spec_a_console/system_detail.html',
        {
            'system': system,
            'review_form': review_form,
            'review_count': review_count,
            'reviews': reviews,
        })


def my_console_systems_view(request):
    """A view to list all ConsoleSystem instances created by the logged-in user."""
    user_systems = ConsoleSystem.objects.filter(
        created_by=request.user).order_by('-created_on')

    return render(
        request,
        'spec_a_console/my_systems.html',
        {
            'user_systems': user_systems,
        })


def create_console_system_view(request):
    """A view to create a new ConsoleSystem."""
    from .forms import ConsoleSystemForm  # Import here to avoid circular import

    if request.method == 'POST':
        form = ConsoleSystemForm(request.POST, request.FILES)
        if form.is_valid():
            console_system = form.save(commit=False)
            console_system.slug = slugify(console_system.name)
            console_system.created_by = request.user
            console_system.save()
            messages.success(request, 'Console system created successfully!')
            return redirect('system_detail', slug=console_system.slug)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ConsoleSystemForm()

    return render(request, 'spec_a_console/create_system.html', {'create_form': form})


@login_required
def delete_console_system_view(request, slug):
    system = get_object_or_404(ConsoleSystem, slug=slug)
    if request.user != system.created_by:
        messages.error(request, "You do not have permission to delete this system.")
        return redirect('system_detail', slug=slug)
    if request.method == "POST":
        system.delete()
        messages.success(request, "System deleted successfully.")
        return redirect('index')
    return redirect('system_detail', slug=slug)
