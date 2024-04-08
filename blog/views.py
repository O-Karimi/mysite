from django.shortcuts import render

# Create your views here.
def blog(requeset):
    return render(requeset,'blog.html')