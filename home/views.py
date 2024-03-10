from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

from event.models import Event
from alliance.models import Group
from actu.models import Actu

# Create your views here.

def home(request) -> render:
    actus = Actu.objects.all().order_by('-date')[:3]
    actus = reversed(actus)
    print(actus)
    
    events = Event.objects.all().order_by('-id')[:3]
    events = reversed(events)

    groups = Group.objects.all().order_by('-id')[:3]
    groups = reversed(groups)

    return render(request, "pages/home.html", context={'actus': actus, 'events': events, 'groups': groups})

@user_passes_test(lambda u: u.is_superuser)
def admin(request) -> render:
    return render(request, "pages/admin.html")