from django.urls import path
from django.conf.urls import handler404 , handler500
from . import views

urlpatterns = [
    #/wiki/
    path("", views.index, name="index"),
    #/wiki/create
    path("create/" , views.create , name="create"),
    #/wiki/string
    path("<str:name>/" , views.detail , name="detail"),

    
]

# handler404 = views.error_404
# handler500 = views.error_500
