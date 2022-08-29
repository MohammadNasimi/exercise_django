from django.urls import path
from books.views import BookAPIView,BookApiViewDetail
urlpatterns = [
    path('list_book/', BookAPIView.as_view(), name = 'list_book'),
    path('detail/<int:pk>/',BookApiViewDetail.as_view(),name = 'dtail_book')
    
]
