from django.shortcuts import render
import datetime
from django import template
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def index_1(request):
    return render(request, 'index_1.html', {})

def contact(request):
    return render(request, 'contact.html', {}) 

def blog(request):
    return render(request, 'blog.html', {})

#def main(request):
    # return render(request, 'main.html', {})

def prevention(request):
    return render(request, 'prevention.html', {})

def single(request):
    return render(request, 'single.html', {})

def symptoms(request):
    return render(request, 'symptoms.html', {})

def how_to_prevent(request):
    return render(request, 'prevention.html', {})


