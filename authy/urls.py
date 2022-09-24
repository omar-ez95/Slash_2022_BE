from django.urls import path

from . import views
from django.contrib.auth import views as authViews 
from django.urls import path, include
from .api import *
from knox import views as knox_views

urlpatterns = [
	# path('api/auth', include('knox.urls')),
	path('api/auth/register', RegisterAPI.as_view(), name = "Register"),
	path('login', LoginAPI.as_view(), name = "LogIn"),
	path('user_details', UserDetails.as_view(), name = "UserDetails"),

	path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),

   	path('passwordreset/', authViews.PasswordResetView.as_view(), name='password_reset'),
   	path('passwordreset/done', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
   	path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   	path('passwordreset/complete/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]