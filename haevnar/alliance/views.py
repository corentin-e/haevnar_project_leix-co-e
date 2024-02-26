from django.http import HttpResponseRedirect

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .models import Group

# Create your views here.
class Groups(ListView):
    model = Group
    queryset = Group.objects.filter(approved=True)
    template_name = "pages/alliance.html"

class CreateGroup(CreateView):
    template_name = "pages/group_creation.html"
    success_url = "/alliance"

    model = Group
    fields = ["name", "description", "status", "logo"]

class Management(ListView):
    model = Group
    template_name = "pages/management.html"

class UpdateGroup(UpdateView):
    model = Group
    fields = ["name", "description", "status", "logo"]
    template_name = "pages/group_update.html"
    success_url = "/alliance/management"


def revoke_group(_, id: int) -> HttpResponseRedirect:
    group = Group.objects.get(pk=id)
    group.approved = False
    group.save()
    return HttpResponseRedirect("/alliance/management")

def approve_group(_, id: int) -> HttpResponseRedirect:
    alliance = Group.objects.get(pk=id)
    alliance.approved = True
    alliance.save()
    return HttpResponseRedirect("/alliance/management")