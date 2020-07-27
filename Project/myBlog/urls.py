from django.urls import path
from . import views
# . means the current directory

urlpatterns = [
    #we want this to be our homepage so we leave the string empty
    path('', views.homepage, name='blog-homepage'),
    path('about', views.about, name='blog-about')
]