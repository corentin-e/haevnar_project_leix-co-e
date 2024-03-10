from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test

from utils import SuperuserTestMixin

from .models import Actu

# Create your views here.
class CreateActu(CreateView, SuperuserTestMixin):
    template_name = "pages/actus_creation.html"
    success_url = "/actus/"

    model = Actu
    fields = ["title", "description", "date", "image"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    

class Management(ListView, SuperuserTestMixin):
    model = Actu
    template_name = "pages/actus_management.html"


@user_passes_test(lambda u: u.is_superuser)
def delete_actu(request, pk: int) -> HttpResponseRedirect:
    if request.user.is_superuser:
        actu = Actu.objects.get(pk=pk)
        actu.delete()
    return HttpResponseRedirect("/actus/")