from django.urls import path

from . import views
from django.contrib.auth import views as authViews 
from django.urls import path, include
from .api import *
from knox import views as knox_views

urlpatterns = [
	# path('api/auth', include('knox.urls')),
	path('articles', TableItemsViewSet.as_view(), name = "articles"),
	path('article/<str:pk>', article_view,  name = "article"),
	path('discources/<str:articleId>', discources_view,  name = "discources"),
	path('discource/post/<str:id>', discources_post_view,  name = "discources"),
	path('msgs/<str:id>', msg_view,  name = "msgs"),
	path('msgs/post/<str:id>', msg_post_view,  name = "msg_post_view"),
]