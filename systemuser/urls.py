from django.urls import path
from . import views 


urlpatterns = [
    path('', views.login_process, name='login'),
    path('logout/', views.logout_process, name='logout'),
    path('voter/view_live_voters_counter/', views.view_live_voters_counter, name='view_voter_counter'),
    path('voter/get_voters/', views.fetch_voter_data, name='fetch_voter_data'),
    path('voter/create/', views.register_voter, name='register_voter'),
    path('voter/view/', views.view_voter, name='view_voter'),
    path('voter/<int:id>/update/', views.update_voter, name='update_voter'),
    path('voter/<int:id>/delete/', views.delete_voter, name='delete_voter'),


    path('employee/create/', views.register_employee, name='register_employee'),
    path('employee/view/', views.view_employee, name='view_employee'),
    path('employee/<int:id>/update/', views.update_employee, name='update_employee'),
    path('employee/<int:id>/delete/', views.delete_employee, name='delete_employee'),

]