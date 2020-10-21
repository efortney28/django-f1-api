from django.urls import path
from . import views

urlpatterns = [
    path('', views.gp_list),
    path('/<int:pk>/', views.gp_detail),
]