from django.urls import path
from . import views

urlpatterns = [
    path('', views.drivers_list),
    path('/<int:pk>/', views.driver_detail),
    path('/current/', views.current_driver_list)
]