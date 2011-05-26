from django.conf.urls.defaults import patterns, include, url
from agendaapp.views import personas
 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
 
urlpatterns = patterns('',
    (r'^agenda/', personas),
    (r'^admin/', admin.site.urls),
)
