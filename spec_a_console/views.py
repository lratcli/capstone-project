from django.shortcuts import redirect, render  # type: ignore
from django.shortcuts import get_object_or_404  # type: ignore
from django.contrib.auth.decorators import login_required  # type: ignore
from django.views import generic  # type: ignore
from django.utils.text import slugify  # type: ignore
from django.http import Http404  # type: ignore
from django.contrib import messages  # type: ignore
from django.db.models import Avg  # for average rating calc # type: ignore
# Below: for paginating my systems view
from django.core.paginator import Paginator  # type: ignore
from .models import ConsoleSystem
from .forms import SystemReviewForm


class ConsoleSystemListView(generic.ListView):
    """
    A view to list all approved ConsoleSystem instances.
    Paginated to show 6 systems per page.
    """
    model = ConsoleSystem
    template_name = 'spec_a_console/index.html'
    context_object_name = 'console_systems'
    paginate_by = 6
    queryset = ConsoleSystem.objects.filter(
        approval=1).order_by('-created_on')


def console_system_detailed_view(request, slug):
    """
    A view to show details of a specific ConsoleSystem.
    Also handles review submission and display.

    **Context**
    ``system``: An instance of :model: `spec_a_console.ConsoleSystem`
    ``reviews``: All instances of :model: `spec_a_console.SystemReview`
         related to the ConsoleSystem instance.

    **Template:**
    :template: `spec_a_console/system_detail.html`

    An instance of :model: `spec_a_console.SystemReview` can be created
    by users to provide feedback on the ConsoleSystem.
    """
    system = get_object_or_404(ConsoleSystem, slug=slug)

    # Only show unapproved systems if accessed by their creator
    if system.approval != 1 and system.created_by != request.user:
        raise Http404("No ConsoleSystem matches the given query.")

    if system.approval != 1 and system.created_by == request.user:
        messages.info(request, "This system is awaiting approval.")

    # add reviews of the system here
    reviews = system.reviews.filter().order_by('-created_on')
    review_count = system.reviews.filter(approved=True).count()

    # calculate average rating from approved reviews only
    approved_reviews = reviews.filter(approved=True)
    avg_rating = approved_reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    avg_rating = round(avg_rating, 1)

    # Handle review submission
    review_form = SystemReviewForm()
    user_has_reviewed = False
    user_is_creator = (request.user.is_authenticated and
                       request.user == system.created_by)

    # Check if user is valid reviewer and has already reviewed the system
    if request.user.is_authenticated and not user_is_creator:
        user_has_reviewed = system.reviews.filter(
            reviewer=request.user).exists()

        if request.method == "POST":
            if user_has_reviewed:
                messages.error(
                    request,
                    "You have already submitted a review for this system.")
            else:
                review_form = SystemReviewForm(data=request.POST)
                if review_form.is_valid():
                    review = review_form.save(commit=False)  # get ref no save
                    review.reviewer = request.user  # finsih populating form
                    # get ref to post review is being put on
                    review.system = system
                    review.save()  # now time to save
                    # Below: send message to user confirming submission
                    messages.add_message(
                        request, messages.SUCCESS,
                        'Review submitted and awaiting approval')
                    # Redirect to the same page to prevent resubmission
                    return redirect('system_detail', slug=system.slug)
    elif request.method == "POST":
        messages.error(request, "You must be logged in to leave a review.")

    return render(
        request,
        'spec_a_console/system_detail.html',
        {
            'system': system,
            'avg_rating': avg_rating,
            'review_form': review_form,
            'review_count': review_count,
            'reviews': reviews,
            'user_has_reviewed': user_has_reviewed,
            'user_is_creator': user_is_creator,
        })


@login_required
def my_console_systems_view(request):
    """
    A view to list and view all ConsoleSystem instances created
      by the logged-in user.

    Paginated to show 6 systems per page.

    **Context**
    ``user_systems``: All instances of :model: `spec_a_console.ConsoleSystem`
        created by the logged-in user. This list also includes systems
        currently pending approval.

    **Template:**
    :template: `spec_a_console/my_systems.html`
    """
    if not request.user.is_authenticated:
        raise Http404("You must be logged in to view your systems.")
    user_systems = ConsoleSystem.objects.filter(
        created_by=request.user).order_by('-created_on')

    # Paginate with 8 systems per page (change as needed)
    paginator = Paginator(user_systems, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'spec_a_console/my_systems.html',
        {
            # 'user_systems': user_systems,
            'user_systems': page_obj.object_list,
            'page_obj': page_obj,
            'is_paginated': page_obj.has_other_pages(),
        })


@login_required
def create_console_system_view(request):
    """
    A view to create a new ConsoleSystem.
    Only accessible to logged-in users.

    **Context**
    ``create_form``: An instance of :form: `spec_a_console.ConsoleSystemForm`
    ``console_system``: An instance of :model: `spec_a_console.ConsoleSystem`

    **Template:**
    :template: `spec_a_console/create_system.html`
    """

    # Import here to avoid circular import
    from .forms import ConsoleSystemForm

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

    return render(request,
                  'spec_a_console/create_system.html',
                  {'create_form': form})


@login_required
def edit_console_system_view(request, slug):
    """
    A view to edit an existing ConsoleSystem.
    Only the creator of the system can edit it.

    **Context**
    ``form``: An instance of :form: `spec_a_console.ConsoleSystemForm`
    ``system``: An instance of :model: `spec_a_console.ConsoleSystem`

    **Template:**
    :template: `spec_a_console/edit_system.html`
    """
    # Import here to avoid circular import:
    from .forms import ConsoleSystemForm
    system = get_object_or_404(ConsoleSystem, slug=slug)
    if request.user != system.created_by:
        raise Http404("You do not have permission to edit this system.")
    if request.method == "POST":
        form = ConsoleSystemForm(request.POST, request.FILES, instance=system)
        if form.is_valid():
            edited_system = form.save(commit=False)
            edited_system.approval = 0  # Set back to "submitted / unapproved"
            edited_system.save()
            messages.success(request, "System updated successfully.")
            return redirect('system_detail', slug=system.slug)
        # TODO: check this else statement thoroughly
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ConsoleSystemForm(instance=system)
    return render(
        request,
        'spec_a_console/edit_system.html',
        {
            'form': form,
            'system': system
        }
    )


@login_required
def delete_console_system_view(request, slug):
    """
    A view to delete an existing ConsoleSystem.
    Only the creator of the system (or admin via admin panel) can delete it.

    **Context**
    ``system``: An instance of :model: `spec_a_console.ConsoleSystem`

    **Template:**
    :template: `spec_a_console/delete_system.html`
    """
    system = get_object_or_404(ConsoleSystem, slug=slug)
    if request.user != system.created_by:
        messages.error(request,
                       "You do not have permission to delete this system.")
        return redirect('system_detail', slug=slug)
    if request.method == "POST":
        system.delete()
        messages.success(request, "System deleted successfully.")
        return redirect('index')
    return redirect('system_detail', slug=slug)
