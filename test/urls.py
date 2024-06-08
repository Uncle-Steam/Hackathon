from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'site-home'),
    path('about/<str:pk>/', views.about, name = 'site-about'),
    path('add', views.add, name='add')
]