from django.shortcuts import render
from .models import Review

def index(request):
    reviews = Review.objects.all()
    return render(request, 'index.html', {'reviews': reviews})
