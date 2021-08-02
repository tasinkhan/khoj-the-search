from django.conf.urls import url
from django.urls import path, include
from Search.views import search_view, SearchResutListApi
from django_filters.views import FilterView
app_name = "Search"
urlpatterns = [
    path('search/', search_view, name='search'),
    path('search-list/',SearchResutListApi.as_view(), name='search-list'),
]