from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = i18n_patterns('',
    # Examples:
    # url(r'^$', 'WestKyMentoring.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^event/', 'main_site.views.events'),
    url(r'^', include('cms.urls')),\
    url(r'^test/', 'main_site.views.test'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
