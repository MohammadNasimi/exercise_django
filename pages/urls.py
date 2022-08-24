from django.urls import path
from pages.views import homePageView,aboutpageview,blogDetail,blogcreate ,BlogUpdateView
urlpatterns = [
    path('', homePageView.as_view(), name = 'home'),
    path('about', aboutpageview.as_view(), name = 'about'),
    path('detail/<int:pk>/',blogDetail.as_view(),name = 'detail'),
    path('create_blog',blogcreate.as_view(),name = 'create_blog'),
    path('update/<int:pk>',
            BlogUpdateView.as_view(), name='post_edit'), 
]
