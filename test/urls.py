from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='site-index'),
    path('about/', views.about, name='site-about')
]
