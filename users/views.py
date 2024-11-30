from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'users/index.html')

