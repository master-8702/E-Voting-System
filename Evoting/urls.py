"""Evoting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from Evoting.settings import DEBUG, INSTALLED_APPS, MIDDLEWARE
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', include('systemuser.urls')),
    path('admin/', admin.site.urls),
    path('voter/',include('election.urls')),
    path('systemuser/',include('systemuser.urls')),
    path('employee/',include('systemuser.urls')),
    path('referendum/', include('election.urls')),
    # path('referendum_options/', include('election.urls')),
    # path('candidate/', include('election.urls')),
    # path('region/', include('election.urls')),
    # path('polling_station/', include('election.urls')),
    # path('observer/', include('election.urls')),
    path('election/', include('election.urls')),
    path('evoting_api/', include('evoting_api.urls')),


    
] 
# image - media -   
#This one also helps us to display images by referencing the urls that we set in the settings.py file about MEDIA_ROOT and MEDIA_URL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# we added this to use the django debug toolbar 
if settings.DEBUG:
    if 'debug_toolbar.apps.DebugToolbarConfig' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

