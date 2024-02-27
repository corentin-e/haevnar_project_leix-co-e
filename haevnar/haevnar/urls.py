"""
URL configuration for haevnar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from home import views as home_views
from discordlogin import views as auth_views
from alliance import views as alliance_views
from event import views as event_views
from actu import views as actu_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    
    # OAuth2 paths #
    path('oauth2/', auth_views.home, name='oauth2'),
    path('oauth2/login/', auth_views.discord_login, name='oauth2_login'),
    path('oauth2/login/redirect/', auth_views.discord_login_redirect, name='oauth2_login_redirect'),
    
    # Alliance paths #
    path('alliance/', alliance_views.Groups.as_view(), name='alliance'),
    path('alliance/creation/', alliance_views.CreateGroup.as_view(), name='create_group'),
    path('alliance/management/', alliance_views.Management.as_view(), name='manage_alliance'),
    path('alliance/management/<int:pk>/', alliance_views.UpdateGroup.as_view(), name='update_group'),

    path('approve_group/<int:id>/', alliance_views.approve_group, name='approve_group'),
    path('revoke_group/<int:id>/', alliance_views.revoke_group, name='revoke_group'),

    # Event paths #
    path('events/', event_views.Events.as_view(), name='events'),
    path('events/creation/', event_views.CreateEvent.as_view(), name='create_event'),
    path('events/management/', event_views.Management.as_view(), name='manage_events'),

    path('delete_event/<int:id>/', event_views.delete_event, name='delete_event'),

    # Actu paths #
    path('actus/', actu_views.Management.as_view(), name='manage_actus'),
    path('actus/creation/', actu_views.CreateActu.as_view(), name='create_actu'),
    path('delete_actu/<int:pk>/', actu_views.delete_actu, name='delete_actu'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
