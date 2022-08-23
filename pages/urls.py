from django.urls import path
from pages.views import homePageView,aboutpageview
urlpatterns = [
    path('', homePageView.as_view(), name = 'home'),
    path('about', aboutpageview.as_view(), name = 'about')
]
