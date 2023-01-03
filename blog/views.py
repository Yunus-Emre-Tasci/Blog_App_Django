from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category,Blog
from .serializers import CategorySerializer,BlogSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class CategoryView(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    filterset_fields=["name"]
    
class BlogView(ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    permission_classes=["IsAuthenticatedOrReadOnly"]
    filterset_fields=["category"]
    search_fields=["title","content"]