from django.urls import path
from . import views

urlpatterns = [
    path('authorization', views.authorization, name='authorization'),
    path('home_page', views.home_page, name='home-page'),
]
