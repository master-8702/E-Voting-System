from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'voters', views.VoterViewSet)
router.register(r'referendum', views.ReferendumOptionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='Voter' )),
]