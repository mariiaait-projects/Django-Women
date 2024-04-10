from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Women\'s app')

def cats(request):
    return HttpResponse('<h1>Cats</h1>')