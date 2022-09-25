from attr import field
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
from django.contrib.auth.models import Group


class ArticleSerializer(serializers.ModelSerializer):

  class Meta:
    model = Article
    fields = '__all__'

class DiscourceSerializer(serializers.ModelSerializer):
  username = serializers.SerializerMethodField()
  class Meta:
    model = Discource
    fields = '__all__'
  def get_username(self,obj):
        return obj.user.username 

class MessageSerializer(serializers.ModelSerializer):
  username = serializers.SerializerMethodField()
  class Meta:
    model = Message
    fields = '__all__'
  def get_username(self,obj):
        return obj.user.username 