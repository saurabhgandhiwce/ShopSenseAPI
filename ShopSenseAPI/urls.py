from django.conf.urls import include, url
from django.contrib import admin
from Movies.views import MovieView
urlpatterns = [
    # Examples:
    # url(r'^$', 'ShopSenseAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^movies/', MovieView.as_view())
]
