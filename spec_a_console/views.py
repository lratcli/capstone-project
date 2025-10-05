from django.shortcuts import render, get_object_or_404, reverse  # noqa: F401, E501, # type: ignore
from django.views import generic  # type: ignore

from django.http import HttpResponse

from .models import ConsoleSystem, SystemReview

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
    queryset = ConsoleSystem.objects.filter(approval=1)
    system = get_object_or_404(queryset, slug=slug)

    # TODO: add reviews of the system here
    # reviews = system.reviews.all().order_by('-created_on')

    # Create a new form, so user can add another comment if they wish
    review_form = SystemReviewForm()

    return render(
        request,
        'spec_a_console/system_detail.html',
        {
            'system': system,
            # 'reviews': reviews,
            'review_form': review_form,
        })
