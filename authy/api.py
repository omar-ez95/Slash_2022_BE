from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from authy.models import Profile
from django.db import transaction
from django.conf import settings
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from knox.models import AuthToken
from .models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes

from django.db.models import Q
from django.core.paginator import Paginator
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from .serializers import * 
# Register API
class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })

# Login API
class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer
  # permission_classes = [Kellner]

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    _, token = AuthToken.objects.create(user)
    token = AuthToken.objects.create(user)[1]
    
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": token
    })

# User Details API
class UserDetails(generics.GenericAPIView):
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]

  def get(self, request, *args, **kwargs):
    user = request.user
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data
    })


# Get User API
class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user


@api_view(['GET', ])
def api_profile_details_view(request, id):
  try:
    user = get_object_or_404(User, id=id)
    profile = get_object_or_404(Profile, user=user)
  except User.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == "GET":
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

@api_view(['PUT', ])
def api_edit_profile_view(request, id):
  try:
    # user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, id=id)

  except User.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == "PUT":
    serializer = ProfileSerializer(profile, data=request.data)
    data={}
    if serializer.is_valid():
      serializer.save()
      data["success"] = "updated successful"
      return Response(serializer.data)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

