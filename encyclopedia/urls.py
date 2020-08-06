from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entryform/", views.entryform, name="entryform"),
    path("wiki/<str:entry>", views.showentry, name="showentry")
]
