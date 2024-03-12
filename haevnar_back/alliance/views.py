from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from rest_framework import viewsets

from .models import Group, Member, GroupSerializer, MemberSerializer
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    def get_queryset(self):
        return Member.objects.filter(group=self.kwargs['group'])
    

@user_passes_test(lambda u: u.is_superuser)
def revoke_group(_, id: int) -> HttpResponseRedirect:
    group = Group.objects.get(pk=id)
    group.status = Group.Status.REJECTED
    group.save()
    return HttpResponseRedirect("/alliance/")

@user_passes_test(lambda u: u.is_superuser)
def approve_group(_, id: int) -> HttpResponseRedirect:
    alliance = Group.objects.get(pk=id)
    alliance.status = Group.Status.APPROVED
    alliance.save()
    return HttpResponseRedirect("/alliance/")