
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login',views.my_login,name='login'),

    # menagement Restuarant&Menu
    path('restaurant/', views.management, name='management'),
    path('restaurant/add/', views.addRestaurant, name='addRestaurant'),
    path('restaurant/food/add/<int:id>/', views.addFood, name='addFood'),
    path('restautant/delete/<int:id>/', views.deleteRestaurant, name='deleteRestaurant'),
    path('restaurant/food/<int:res_id>/delete/<int:food_id>/', views.deleteFood, name='deleteFood')
    # path('restaurant/edit/<int:id>/', views.editRestaurant, name='editRestaurant'),
    # path('restaurant/food/edit/<int:id>/', views.editFood, name='editFood')
]