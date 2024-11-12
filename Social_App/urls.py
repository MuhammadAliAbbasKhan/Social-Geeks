

from django.contrib import admin
from django.urls import path , include

#  Libraries Imported  For Uploading Media In Project 
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SocialGeek.urls')),
] + static(settings.MEDIA_URL , document_root  = settings.MEDIA_ROOT)
