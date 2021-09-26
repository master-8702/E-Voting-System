from django.urls import path
from . import views 


urlpatterns = [
    # path('', views.index, name='index'),
    # path('voter/hello/', views.index1, name='index3'),
    path('party/create/', views.register_party, name='register_party'),
    path('party/view/', views.view_party, name='view_party'),
    path('party/<int:id>/update/', views.update_party, name='update_party'),
    path('party/<int:id>/delete/', views.delete_party, name='delete_party'),
    
    path('create_election/', views.register_election, name='register_election'),
    path('view_election/', views.view_election, name='view_election'),
    path('<int:id>/update_election/', views.update_election, name='update_election'),
    path('<int:id>/delete_election/', views.delete_election, name='delete_election'),
    
    
    path('referendum/create_referendum/', views.register_referendum, name='register_referendum'),
    path('referendum/view_referendum/', views.view_referendum, name='view_referendum'),
    path('referendum/<int:id>/update_referendum/', views.update_referendum, name='update_referendum'),
    path('referendum/<int:id>/delete_referendum/', views.delete_referendum, name='delete_referendum'),


    path('create_referendum_options/', views.register_referendum_options, name='register_referendum_options'),
    path('view_referendum_options/', views.view_referendum_options, name='view_referendum_options'),
    path('<int:id>/update_referendum_options/', views.update_referendum_options, name='update_referendum_options'),
    path('<int:id>/delete_referendum_options/', views.delete_referendum_options, name='delete_referendum_options'),


    path('create_candidate/', views.register_candidate, name='register_candidate'),
    path('view_candidate/', views.view_candidate, name='view_candidate'),
    path('<int:id>/update_candidate/', views.update_candidate, name='update_candidate'),
    path('<int:id>/delete_candidate/', views.delete_candidate, name='delete_candidate'),


    path('create_election_region/', views.register_election_region, name='register_election_region'),
    path('view_election_region/', views.view_election_region, name='view_election_region'),
    path('<int:id>/update_election_region/', views.update_election_region, name='update_election_region'),
    path('<int:id>/delete_election_region/', views.delete_election_region, name='delete_election_region'),


    path('create_region/', views.register_region, name='register_region'),
    path('view_region/', views.view_region, name='view_region'),
    path('<int:id>/update_region/', views.update_region, name='update_region'),
    path('<int:id>/delete_region/', views.delete_region, name='delete_region'),

    path('create_polling_station/', views.register_polling_station, name='register_polling_station'),
    path('view_polling_station/', views.view_polling_station, name='view_polling_station'),
    path('<int:id>/update_polling_station/', views.update_polling_station, name='update_polling_station'),
    path('<int:id>/delete_polling_station/', views.delete_polling_station, name='delete_polling_station'),


    path('create_observer/', views.register_observer, name='register_observer'),
    path('view_observer/', views.view_observer, name='view_observer'),
    path('<int:id>/update_observer/', views.update_observer, name='update_observer'),
    path('<int:id>/delete_observer/', views.delete_observer, name='delete_observer'),



    path('voter/view_election_result/', views.view_election_result, name='view_election_result'),
    path('voter/verify_vote_universally/', views.verify_vote_universally, name='verify_vote_universally'),
    path('voter/verify_vote_individually/', views.verify_vote_individually, name='verify_vote_individually'),
    path('voter/view_live_voters_counter/', views.view_live_voters_counter, name='view_voter_counter'),
    path('voter/get_voters/', views.fetch_voter_data, name='fetch_voter_data'),
    path('voter/view_live_vote_counter/', views.view_live_vote_counter, name='view_vote_counter'),
    path('voter/get_votes/', views.fetch_vote_data, name='fetch_vote_data'),
    path('voter/create/', views.register_voter, name='register_voter'),
    path('voter/view/', views.view_voter, name='view_voter'),
    path('voter/<int:id>/update/', views.update_voter, name='update_voter'),
    path('voter/<int:id>/delete/', views.delete_voter, name='delete_voter'),
    path('voter/cast_ballot/', views.cast_ballot, name='cast_ballot'),


    path('view_analytics/', views.view_analytics, name='view_analytics'),
    path('referendum/view_referendum_result/', views.view_referendum_result, name='view_referendum_result'),



]