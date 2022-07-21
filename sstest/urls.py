from django.urls import path
from . import views

app_name = 'sstest'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('qSet/', views.qSet, name='qSet'),
    path('result/', views.result, name='result'),
]