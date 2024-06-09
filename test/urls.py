from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='site-index'),
    path('index/', views.index, name='site-index'),
    path('login', views.login, name='site-login'),
    path('signup/', views.signup, name='site-signup'),
    path('signup', views.insight),
    path('dashboard', views.dashboard),
    path('investor/', views.investor),
    path('insight', views.insight)
]
