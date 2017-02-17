
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #Include all urls in the login app
    url(r'^login/', include('login.urls')),
]
