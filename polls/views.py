from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse('Hello world. You are at the index page now!')

# Create your views here.