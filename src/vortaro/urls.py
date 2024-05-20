from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('query/', views.index, name="index"),
    path("query/<str:query_term>", views.get_madde, name='madde'),
]
