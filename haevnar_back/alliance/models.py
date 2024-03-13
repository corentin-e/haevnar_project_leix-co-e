from django.db import models
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

# Create your models here.
class Group(models.Model):
    class GroupType(models.TextChoices):
        ESCOUADE = "Esc", _("Escouade")
        CORPORATION = "Corp", _("Corporation")
        ALLIANCE = "All", _("Alliance")

    class Status(models.TextChoices):
        PENDING = "Att", _("Attente")
        APPROVED = "App", _("Approuve")
        REJECTED = "Rej", _("Rejete")


    name = models.CharField(max_length=100, null=False)
    tag = models.CharField(max_length=10, null=False)
    description = models.TextField()
    type = models.CharField(default=GroupType.CORPORATION, 
                              choices=GroupType.choices,
                              max_length=4,
                              null=False
                            )
    status = models.CharField(default=Status.PENDING, 
                              choices=Status.choices,
                              max_length=3,
                              null=False
                            )
    logo = models.ImageField(blank=True, null=True)
    main_color = models.CharField(max_length=7, default="#ffffff", null=False)
    secondary_color = models.CharField(max_length=7, default="#000000", null=False)
    rsi_url = models.URLField()

class Member(models.Model):
    discord_username = models.CharField(max_length=100)
    rsi_handle = models.CharField(max_length=100)
    leader = models.BooleanField(default=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

        
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
