from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Event

# Create your views here.
class Events(ListView):
    model = Event
    template_name = "pages/events.html"

class CreateEvent(CreateView):
    template_name = "pages/event_creation.html"
    success_url = "/events/"

    model = Event
    fields = ["name", "description", "date", "emplacement"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class Management(ListView):
    model = Event
    template_name = "pages/events_management.html"


def delete_event(_, id: int) -> HttpResponseRedirect:
    event = Event.objects.get(pk=id)
    event.delete()
    return HttpResponseRedirect("/events/management")