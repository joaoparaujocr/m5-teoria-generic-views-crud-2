from django.urls import path
from .views import AuthorView, CreateBookView, BookDetailView, ListBookView

urlpatterns = [
    path('books/', ListBookView.as_view()),
    path('books/author/<int:author_id>/', CreateBookView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('author/', AuthorView.as_view())
]
