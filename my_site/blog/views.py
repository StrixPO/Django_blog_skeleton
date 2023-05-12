from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug": "travel",
        "image": "mount.jpg",
        "autor": "Rusar",
        "date": date(2002,5, 10),
        "title": "Travelling",
        "excert": "Lets make something together",
    },
    {
        "slug": "code_devlopment",
        "image": "code.jpeg",
        "autor": "Rusar",
        "date": date(2002,5, 10),
        "title": "Code development",
        "excert": "Lets make something together",
    },
    {
        "slug": "exercise",
        "image": "workout.jpg",
        "autor": "Rusar",
        "date": date(2002,5, 10),
        "title": "Workout",
        "excert": "Lets make something together",
    },
]

def get_date(post):
    return post['date']

def index(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts":latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def posts_detail(request, slug):
    identified_post=next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })