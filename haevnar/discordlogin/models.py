from django.db import models
from .managers import DiscordUserManager

# Create your models here.

class DiscordUser(models.Model):
    objects = DiscordUserManager()

    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    public_flags = models.IntegerField(max_length=100)
    flags = models.IntegerField(max_length=100)
    locale = models.CharField(max_length=100)
    mfa_enabled = models.BooleanField()
    last_login = models.DateTimeField(null=True)


    # Django User fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    def get_username(self):
        return self.username
    
    