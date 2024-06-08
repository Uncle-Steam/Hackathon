from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='site-index'),
    path('index/', views.index, name='site-index'),
    path('login', views.login, name='login')
]
