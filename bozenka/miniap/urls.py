from django.urls import path

from . import views

urlpatterns = [
    path('mini/', views.models_list)
]