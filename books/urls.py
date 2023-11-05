from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home,name='books-home'),
    path('category/',views.category,name='book-category'),
    path('sci-fi/',views.Sci_fi,name='book-sci_fi'),
    path('philosophy/',views.philosphy,name='book-philosophy'),
    path('horror/',views.horror,name='book-horror'),
    path('mystery/',views.mystery,name='book-fiction'),
    path('fantasy/',views.fantasy,name='book-mystery'),
    path('educational/',views.education,name='book-education'),
    path('dsytopia/',views.dsytopia,name='book-dsytopia'),
    path('about/',views.about,name='book-about'),
    path('bhome/',views.BHome,name='book-bhome'),
    path('manga/',views.manga,name='book-manga'),
    path('classics/',views.classics,name='book-clssics'),
    path('cookbook/',views.cookbook,name='book-cookbook'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
    path('book-search/', views.book_search, name='book_search'),
    # add all category of books sci-fi,horror,adventure and all
]
