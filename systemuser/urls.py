from django.urls import path
from . import views 


urlpatterns = [
    path('', views.login_process, name='login'),
    path('voter_login/', views.voter_login, name='voter_login'),
    path('logout/', views.logout_process, name='logout'),



    path('employee/create/', views.register_employee, name='register_employee'),
    path('employee/view/', views.view_employee, name='view_employee'),
    path('employee/<int:id>/update/', views.update_employee, name='update_employee'),
    path('employee/<int:id>/delete/', views.delete_employee, name='delete_employee'),

]