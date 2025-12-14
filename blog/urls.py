from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("all_articles/", views.AllArticles.as_view(), name="all_articles"),
]
