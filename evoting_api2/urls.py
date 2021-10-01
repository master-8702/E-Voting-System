from django.urls import path
from . import views

urlpatterns = [

    path('', views.apiOverView, name='api-overview'),
    path('region-list/', views.regionList, name='region-list'),
    path('region-detail/<int:id>/', views.regionDetail, name='region-detail'),
    path('region-create/', views.regionCreate, name='region-create'),
    path('region-update/<int:id>/', views.regionUpdate, name='region-update'),
    path('region-delete/<int:id>/', views.regionDelete, name='region-delete'),

]