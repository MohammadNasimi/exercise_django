from django.urls import path
from books.views import BookAPIView
urlpatterns = [
    path('list_book/', BookAPIView.as_view(), name = 'list_book'),
]
