from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('profile/',views.profile,name='student-profile'),
    path('bookissued/',views.bi,name='student-bookissued'),
]
