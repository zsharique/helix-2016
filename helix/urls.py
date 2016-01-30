from django.conf.urls import include, url
from django.contrib import admin
import app.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'helix.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.landing_view'),
]
