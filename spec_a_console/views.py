from django.shortcuts import render, get_object_or_404, reverse  # noqa: F401, E501, # type: ignore
from django.views import generic  # type: ignore

from django.http import HttpResponse

from .models import HypotheticalSystem, SystemReview


# Create your views here.
def index(request):
    return HttpResponse("Hello, this is the spec_a_console index page.")


class HypotheticalSystemListView(generic.ListView):
    """A view to list all approved HypotheticalSystem instances."""
    model = HypotheticalSystem
    template_name = 'spec_a_console/index.html'
    context_object_name = 'hypothetical_systems'
    paginate_by = 10
    queryset = HypotheticalSystem.objects.filter(
        approval=1).order_by('-created_on')


def hypothetical_system_detail_view(request, slug):
    """A view to show details of a specific HypotheticalSystem."""
    queryset = HypotheticalSystem.objects.filter(approval=1)
    system = get_object_or_404(queryset, slug=slug)

    # TODO: add reviews of the system here
    # reviews = system.reviews.all().order_by('-created_on')

    return render(
        request,
        'spec_a_console/system_detail.html',
        {
            'system': system,
            # 'reviews': reviews,
        })
