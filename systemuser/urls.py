from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    # path('voter/hello/', views.index1, name='index3'),
    path('voter/create/', views.register_voter, name='register_voter'),
    path('voter/view/', views.view_voter, name='view_voter'),
    path('voter/<int:id>/update/', views.update_voter, name='update_voter'),
    path('voter/<int:id>/delete/', views.delete_voter, name='delete_voter'),


    path('employee/create/', views.register_employee, name='register_employee'),
    path('employee/view/', views.view_employee, name='view_employee'),
    path('employee/<int:id>/update/', views.update_employee, name='update_employee'),
    path('employee/<int:id>/delete/', views.delete_employee, name='delete_employee'),

]