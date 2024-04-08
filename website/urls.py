from django.urls import path
from website.views import webview

app_name = 'website'

urlpatterns = [
    path('',webview,name='home'),
]
