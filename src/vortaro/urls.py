from django.urls import path
from . import views


urlpatterns = [
    path('', views.query_madde, name='maddes'),
    path("<str:query_term>", views.query_madde, name='madde'),
]