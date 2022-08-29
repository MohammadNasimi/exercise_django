from django.urls import path
from books.views import list_book_viewAPI
urlpatterns = [
    path('list_book', list_book_viewAPI.as_view(), name = 'list_book'),
]
