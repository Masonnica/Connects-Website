from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tools/', views.tools, name='tools'),
    path('library/', views.library, name='library'),
    path('documents/', views.documents, name='documents'),
]
