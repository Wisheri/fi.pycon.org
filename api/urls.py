from django.conf.urls.defaults import patterns, url, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

YEAR = settings.YEAR

urlpatterns = patterns(
    '',
    url(r'^api/admin/', include(admin.site.urls)),

    # API
    url(r'^$', 'api.pyconfi%s.views.index' % YEAR),
    url(r'^api/%s/register/$' % YEAR,
        'api.pyconfi%s.views.register' % YEAR),
    url(r'^api/%s/seats_left$' % YEAR,
        'api.pyconfi%s.views.seats_left' % YEAR),
    url(r'^api/%s/country$' % YEAR,
        'api.pyconfi%s.views.autocomplete_country' % YEAR),
)

if settings.DEBUG:
    urlpatterns += static('/', document_root='..')
