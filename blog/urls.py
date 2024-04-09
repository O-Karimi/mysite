from django.urls import path
from blog.views import blog , blog_single

app_name = 'blog'

urlpatterns = [
    path('',blog,name='blog'),
    path('single/',blog_single,name='single-blog'),
]
