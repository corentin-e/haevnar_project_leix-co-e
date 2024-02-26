from django.shortcuts import render

from event.models import Event
from alliance.models import Group

# Create your views here.

def home(request) -> render:
    events = Event.objects.all().order_by('-id')[:3]
    events = reversed(events
                      )
    groups = Group.objects.all().order_by('-id')[:3]
    groups = reversed(groups)

    return render(request, "pages/home.html", context={'events': events, 'groups': groups})