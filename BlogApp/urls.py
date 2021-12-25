
from . import views

from django.urls import path


urlpatterns = [

    # path('', views.index, name='index'),
    # """for function based views"""
    # path('home/', views.Home, name='home'),
    # path('about/', views.About, name='about'),
    # path('contact/', views.Contact, name='contact'),
    # path('login/', views.Login, name='login'),
    # path('register/', views.Register, name='register'),

    # """For Class Based Views """
    path('', views.Home.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('about/', views.About.as_view(), name='about'),
    path('blogs/', views.Blogs.as_view(), name='blogs'),
    path('logout/', views.Logout, name='logout'),
]
