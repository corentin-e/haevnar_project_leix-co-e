from django.contrib.auth.backends import BaseBackend
from .models import DiscordUser

class DiscordAuthBackend(BaseBackend):
    def authenticate(self, request, user)-> DiscordUser:
        try:
            user = DiscordUser.objects.get(id=user['id'])
            return user
        except DiscordUser.DoesNotExist:
            new_user = DiscordUser.objects.create_new_discord_user(user)
            return new_user

    def get_user(self, user_id):
        try:
            return DiscordUser.objects.get(pk=user_id)
        except DiscordUser.DoesNotExist:
            return None