
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login', views.my_login, name='login'),
    path('logout', views.my_logout, name='logout'),

    # menagement Restuarant&Menu
    path('restaurant/', views.management, name='management'),
    path('restaurant/add/', views.addRestaurant, name='addRestaurant'),
    # path('restaurant/detailRestaurant/', views.detailRestaurant, name='detailRestaurant'),
    path('restaurant/food/add/<int:id>/', views.addFood, name='addFood'),
    path('restautant/delete/<int:id>/',
         views.deleteRestaurant, name='deleteRestaurant'),
    path('restaurant/food/<int:res_id>/delete/<int:food_id>/',
         views.deleteFood, name='deleteFood'),
    path('restaurant/edit/<int:id>/', views.editRestaurant, name='editRestaurant'),
    path('manageOrder', views.manageOrder, name='manageOrder'),
    path('restaurant/food/<int:res_id>/edit/<int:food_id>/',
         views.editFood, name='editFood'),
     path('Order/confirmOrder/<int:order_id>/',views.confirmOrder,name='confirmOrder'),
     path('Order/cancelOrder/<int:order_id>/',views.cancelOrder,name='cancelOrder')
]
