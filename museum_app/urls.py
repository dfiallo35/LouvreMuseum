from django.urls import path
from django.views import View
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('catalog/', views.catalog, name='catalog')
]
