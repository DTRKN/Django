from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('home/', index, name='home'), 
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contant/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),   
]