from django.shortcuts import render

from django.http import HttResponse

def home(request):
    return HttpResponse('Hello, World!')

# Create your views here.
