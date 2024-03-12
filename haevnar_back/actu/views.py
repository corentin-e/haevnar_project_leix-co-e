from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from django.contrib.auth.decorators import user_passes_test

from utils import SuperuserTestMixin

from .models import Actu, ActuSerializer

# Create your views here.
class CreateActu(APIView, SuperuserTestMixin):
    model = Actu
    fields = ["title", "description", "date", "image"]

class Management(APIView, SuperuserTestMixin):
    model = Actu
    template_name = "pages/actus_management.html"

class ActuViewSet(viewsets.ModelViewSet):
    queryset = Actu.objects.all()
    serializer_class = ActuSerializer



@user_passes_test(lambda u: u.is_superuser)
def delete_actu(request, pk: int):
    if request.user.is_superuser:
        actu = Actu.objects.get(pk=pk)
        actu.delete()