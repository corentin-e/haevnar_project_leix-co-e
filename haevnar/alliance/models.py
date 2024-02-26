from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Group(models.Model):
    class GroupType(models.TextChoices):
        ESCOUADE = "Esc", _("Escouade")
        CORPORATION = "Corp", _("Corporation")
        ALLIANCE = "All", _("Alliance")


    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(default=GroupType.CORPORATION, 
                              choices=GroupType.choices,
                              max_length=4
                            )
    approved = models.BooleanField(default=False)
    logo = models.ImageField(blank=True, null=True)

