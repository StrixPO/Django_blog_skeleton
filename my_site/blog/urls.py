from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='firstpage'),
    path("posts", views.posts, name='posts'),
    path("posts/<slug>", views.posts_detail, name='info'), #slug - posts/myfirstpost
]

