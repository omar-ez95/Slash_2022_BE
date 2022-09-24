
from . import views
from django.contrib.auth import views as authViews 
from django.urls import path, include
from .api import *
from knox import views as knox_views

urlpatterns = [
	# path('api/auth', include('knox.urls')),
	path('api/auth/register', RegisterAPI.as_view(), name = "Register"),
	path('login', LoginAPI.as_view(), name = "LogIn"),

	path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),

]