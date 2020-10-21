from django.urls import path
from . import views

urlpatterns = [
    path('', views.season_list),
    path('/<str:year>/', views.season_detail)
]