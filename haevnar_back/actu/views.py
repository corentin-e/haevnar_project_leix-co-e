from rest_framework import viewsets

from .models import Actu, ActuSerializer
class ActuViewSet(viewsets.ModelViewSet):
    queryset = Actu.objects.all()
    serializer_class = ActuSerializer
