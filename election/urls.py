from django.urls import path
from . import views 


urlpatterns = [
    # path('', views.index, name='index'),
    # path('voter/hello/', views.index1, name='index3'),
    path('party/create/', views.register_party, name='register_party'),
    path('party/view/', views.view_party, name='view_party'),
    path('party/<int:id>/update/', views.update_party, name='update_party'),
    path('party/<int:id>/delete/', views.delete_party, name='delete_party'),
    
    path('election/create_election/', views.register_election, name='register_election'),
    path('election/view_election/', views.view_election, name='view_election'),
    path('election/<int:id>/update_election/', views.update_election, name='update_election'),
    path('election/<int:id>/delete_election/', views.delete_election, name='delete_election'),
    
    

]