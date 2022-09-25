from email import message
from django.contrib.auth.models import Permission, PermissionManager
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.mixins import CreateModelMixin,ListModelMixin
from rest_framework.decorators import api_view, permission_classes

class TableItemsViewSet(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        articles = Article.objects.all()
        return articles


@api_view(['GET', ])
def article_view(request, pk):
    try:
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'error': 'there is no article'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def discources_view(request, articleId):
    article = Article.objects.get(id=articleId)
    print(article)
    discources = Discource.objects.filter(articel=article)
    print(discources)
    serializer = DiscourceSerializer(discources, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST', ])
def discources_post_view(request, id):
    request.data['user'] = request.user.id
    article = Article.objects.get(id=id)
    request.data['articel'] = article.id
    serializer = DiscourceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', ])
def msg_view(request, id):
    discource = Discource.objects.get(id=id)
    messages = Message.objects.filter(articel=discource).order_by('-created')
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST', ])
def msg_post_view(request, id):
    request.data['user'] = request.user.id
    discource = Discource.objects.get(id=id)
    request.data['articel'] = discource.id
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)