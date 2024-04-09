from django.shortcuts import render

# Create your views here.
def blog(requeset):
    return render(requeset,'blog/blog.html')

def blog_single(requeset):
    return render(requeset,'blog/single-blog.html')
