from django.urls import path
from blog.views import blogListView,blogUpdateView,blogDetailView, blogDeleteView , blogcreateview
urlpatterns = [
    path('', blogListView.as_view(), name = 'bloglist'),
    path('<int:pk>/edit/',
        blogUpdateView.as_view(), name='blog_edit'),
    path('<int:pk>/',
        blogDetailView.as_view(), name='blog_detail'), 
    path('<int:pk>/delete/',
        blogDeleteView.as_view(), name='blog_delete'),
    path('new/',
        blogcreateview.as_view(), name='blog_new'), 
]
