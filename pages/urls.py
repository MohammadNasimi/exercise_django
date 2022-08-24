from django.urls import path
from pages.views import homePageView,aboutpageview,blogDetail
urlpatterns = [
    path('', homePageView.as_view(), name = 'home'),
    path('about', aboutpageview.as_view(), name = 'about'),
    path('detail/<int:pk>/',blogDetail.as_view(),name = 'detail')
]
