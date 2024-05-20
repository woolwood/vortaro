from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('query', views.search_index, name="search_index"),
    #path('', views.query_madde, name='maddes'),
    path("madde/<str:query_term>", views.get_madde, name='madde'),
]