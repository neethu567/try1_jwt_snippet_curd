from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework import request
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from myapp.models import Snippet, Tag
from myapp.serializers import SnippetCreateUpdateSerializer, SnippetListSerializer, TagSerializer


class SnippetListCreateAPIView(ListCreateAPIView):
    queryset = Snippet.objects.all()
    # queryset_user = User.objects.all()
    # serializer_class = queryset_user
    # permission_classes = [IsAuthenticated]

    # current_user = User.objects.all()
    def get_serializer_class(self):
        if self.request.method == "POST":
            return SnippetCreateUpdateSerializer
        return SnippetListSerializer
    # def create(self,serializer):
    #     serializer.save(user=self.request.user)

class SnippetDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetListSerializer
    lookup_field = "pk"
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return SnippetCreateUpdateSerializer
        return SnippetListSerializer

class TagListView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
