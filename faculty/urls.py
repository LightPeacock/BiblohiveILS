from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('flogin/',views.faculty_login,name='faculty-login'),
    path('profile/',views.profile,name='faculty-profile'),
    path('booksissued/',views.bi,name='faculty-booksissued'),
    path('register/', views.register, name='register'),
]
