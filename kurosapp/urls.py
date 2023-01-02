from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_answer/', views.check_answer, name='check_answer'),
]

