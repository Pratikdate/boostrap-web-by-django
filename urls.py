from django.contrib import admin
from django.urls import path
from app2 import views
from app2.models import post
urlpatterns = [
    
    path("", views.home,
name="home"),
    path("/", views.home,           name="home"),
    path("abouts/",views.about, name="abouts"),
    
    path("services/", views.service, name="services"),
    
    path("blogs/", views.bloghome, name="blogs"),
    path("blog", views.blog, name="blog"),
    path("blogs/<str:slug>", views.blogslug, name="blogslug"),
    path("blog/", views.blog, name="blog"),
    path("useraccount", views.useraccount, name="useraccount"),
    
    path("blog/{{post.slug}}", views.useraccount, name="useraccount"),
    
    path("login", views.loginuser, name="login"),
    path("login/", views.loginuser, name="logins"),
    
    path("logout", views.userlogout, name="logout"),
    
    
    
]