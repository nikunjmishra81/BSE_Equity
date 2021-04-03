from django.urls import path
from .views import CacheDataView

urlpatterns = [
    path('data/', CacheDataView.as_view()),
]
