from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list),
    path('/<int:pk>/', views.team_detail),
    path('/current/', views.current_teams_list),
]