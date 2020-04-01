from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
from blog.models import Blog
from django.contrib.auth.models import User
from django.urls import reverse


def home(request):
    context = {}
    return render(request,'home.html', context)

