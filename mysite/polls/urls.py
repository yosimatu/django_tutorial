from django.urls import path

#from polls import viewsと同じ？
from . import views

urlpatterns = [
        path('', views.index, name='index'),
]
