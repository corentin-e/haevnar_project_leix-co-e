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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from discordlogin import views as auth_views
from alliance import views as alliance_views
from event import views as event_views
from actu import views as actu_views

urlpatterns = [    
    # OAuth2 paths #
    path('oauth2/login/', auth_views.discord_login, name='login'),
    path('oauth2/login/redirect/', auth_views.discord_login_redirect, name='oauth2_login_redirect'),
    
    # Alliance paths #
    ## Group paths ##
    path('alliance/', alliance_views.GroupViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
        }), name='groups'),
    path('alliance/<int:pk>', alliance_views.GroupViewSet.as_view(
        {
            'get': 'retrieve',
            'delete': 'destroy',
            'patch': 'partial_update',
        }), name='single_group'),   
    ## Member paths ##
    path('alliance/<int:group>/members/', alliance_views.MemberViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
        }), name='members'),
    path('alliance/<int:group>/members/<int:pk>', alliance_views.MemberViewSet.as_view(
        {
            'get': 'retrieve',
            'delete': 'destroy',
            'patch': 'partial_update',
            'patch': 'update',
        }), name='single_member'),
    
    # Event paths #
    path('events/', event_views.EventViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
        }), name='events'),
    path('events/<int:pk>', event_views.EventViewSet.as_view(
        {
            'get': 'retrieve',
            'delete': 'destroy',
        }), name='single_event'),   

    # Actu paths #
    path('actus/', actu_views.ActuViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
        }), name='actus'),
    path('actus/<int:pk>', actu_views.ActuViewSet.as_view(
        {
            'get': 'retrieve',
            'delete': 'destroy',
        }), name='single_actu'),   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
