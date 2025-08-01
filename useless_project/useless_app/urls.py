from django.urls import path
from .views import generate_thought_view

urlpatterns = [
    path('generate/', generate_thought_view, name='generate_thought'),
]
