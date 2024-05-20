from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path("madde/<str:query_term>", views.get_madde, name='madde'),
]
