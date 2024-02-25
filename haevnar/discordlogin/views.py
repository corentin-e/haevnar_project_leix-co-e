import os

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import requests


AUTH_URL = os.environ.get('AUTH_URL')
CLIENT_ID = os.environ.get('CLIENT_ID')
SECRET = os.environ.get('SECRET')

# Create your views here.
def home(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"message": "Hello, World!"})

def discord_login(request: HttpRequest):
    return redirect(AUTH_URL)

def discord_login_redirect(request: HttpRequest):
    request_code = request.GET.get('code')
    response = requests.post("https://discord.com/api/oauth2/token", 
                  data={
                    "client_id": CLIENT_ID,
                    "client_secret": SECRET,
                    "grant_type": "authorization_code",
                    "code": request_code,
                    "redirect_uri": "http://localhost:8000/oauth2/login/redirect",
                    "scope": "identify"
                },
                headers={
                    "Content-Type": "application/x-www-form-urlencoded"
                }
    )
    credentials = response.json()
    access_token = credentials.get('access_token')
    response = requests.get("https://discord.com/api/v6/users/@me", headers={
        'Authorization': f'Bearer {access_token}'        
    })

    user = response.json()
    discord_user = authenticate(request=request, user=user)
    login(request, discord_user)

    return JsonResponse({'user': user})