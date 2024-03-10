from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

from utils import SuperuserTestMixin

from .models import Group, Member

### GROUPS DISPLAY AND MANAGEMENT ###
class Groups(ListView):
    model = Group
    queryset = Group.objects.filter(status=Group.Status.APPROVED)
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


### MEMBERS DISPLAY AND MANAGEMENT ###
class MembersViews(ListView):
    model = Member
    template_name = "pages/members_update.html"
    def get_queryset(self):
        return Member.objects.filter(group=self.kwargs['group'])

class MemberEditView(UpdateView, SuperuserTestMixin):
    model = Member
    template_name = "pages/member_update.html"
    fields = ["discord_username", "rsi_handle", "leader"]

    def get_success_url(self):
        return reverse("edit_members", args=[self.kwargs['group']])

class MembersCreateView(CreateView, SuperuserTestMixin):
    model = Member
    template_name = "pages/members_create.html"
    fields = ["discord_username", "rsi_handle", "leader"]

    def get_success_url(self):
        return reverse("edit_members", args=[self.kwargs['group']])

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.group = Group.objects.get(pk=self.kwargs['group'])
        return super().form_valid(form)


@user_passes_test(lambda u: u.is_superuser)
def revoke_group(_, id: int) -> HttpResponseRedirect:
    group = Group.objects.get(pk=id)
    group.status = Group.Status.REJECTED
    group.save()
    return HttpResponseRedirect("/alliance/management")

@user_passes_test(lambda u: u.is_superuser)
def approve_group(_, id: int) -> HttpResponseRedirect:
    alliance = Group.objects.get(pk=id)
    alliance.status = Group.Status.APPROVED
    alliance.save()
    return HttpResponseRedirect("/alliance/management")