from django.shortcuts import render
from django.http import HttpResponse
from .services import get_content

# Create your views here.

def generate_thought_view(request):
    thought = get_content()
    return HttpResponse(thought)