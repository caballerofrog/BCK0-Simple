from django.urls import path
from . import views

urlpatterns = [
    path('', views.showHome, name='home'),
    path('animal/', views.showAnimals, name='animal'),
]