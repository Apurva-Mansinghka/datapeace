from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import UserSerializer
from .models import User
from django.shortcuts import render


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('firstName')
    serializer_class = UserSerializer
