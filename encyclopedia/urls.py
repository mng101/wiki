from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entryform/", views.entryform, name="entryform"),
    path("entryform/<str:entry>", views.entryform, name="entryform"),
    path("randompage/", views.randompage, name="randompage"),
    path("wiki/<str:entry>", views.showentry, name="showentry")
]
