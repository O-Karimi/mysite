from django.shortcuts import render

# Create your views here.
def webview(requeset):
    return render(requeset,'website/index.html')