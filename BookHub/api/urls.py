from django.urls import path, include
from . import views

urlpatterns = [
    path('books/', views.Books.as_view()),
    path('book/<int:pk>/', views.BookDetail.as_view()),
]