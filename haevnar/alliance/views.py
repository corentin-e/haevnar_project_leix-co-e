from django.http import HttpResponseRedirect

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import user_passes_test

from utils import SuperuserTestMixin

from .models import Group

# Create your views here.
class Groups(ListView):
    model = Group
    queryset = Group.objects.filter(approved=True)
    template_name = "pages/alliance.html"

class CreateGroup(CreateView, SuperuserTestMixin):
    template_name = "pages/group_creation.html"
    success_url = "/alliance"

    model = Group
    fields = ["name", "description", "status", "logo"]

class Management(ListView, SuperuserTestMixin):
    model = Group
    template_name = "pages/management.html"

class UpdateGroup(UpdateView, SuperuserTestMixin):
    model = Group
    fields = ["name", "description", "status", "logo"]
    template_name = "pages/group_update.html"
    success_url = "/alliance/management"


@user_passes_test(lambda u: u.is_superuser)
def revoke_group(_, id: int) -> HttpResponseRedirect:
    group = Group.objects.get(pk=id)
    group.approved = False
    group.save()
    return HttpResponseRedirect("/alliance/management")

@user_passes_test(lambda u: u.is_superuser)
def approve_group(_, id: int) -> HttpResponseRedirect:
    alliance = Group.objects.get(pk=id)
    alliance.approved = True
    alliance.save()
    return HttpResponseRedirect("/alliance/management")