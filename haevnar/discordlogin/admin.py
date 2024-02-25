from django.contrib import admin
from django.utils.html import mark_safe

from .models import DiscordUser

# Register your models here.
@admin.register(DiscordUser)
class DiscordUserAdmin(admin.ModelAdmin):
    list_display = ["rendered_avatar", "username", "last_login", "is_active", "is_staff", "is_superuser"]
    readonly_fields = ["rendered_avatar"]

    @admin.display(description="Avatar")
    def rendered_avatar(self, obj):
        return mark_safe(f'<img src="https://cdn.discordapp.com/avatars/{obj.id}/{obj.avatar}.png" width="50" height="50" />')
    
    @admin.display(description="Username")
    def upper_case_name(self, obj):
        return obj.get_username()