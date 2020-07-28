from django.urls import path

from . import views

urlpatterns = [
    #/wiki/
    path("", views.index, name="index"),
    #/wiki/string
    path("<str:name>/" , views.detail , name="detail"),
]
