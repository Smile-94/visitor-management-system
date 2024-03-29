
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Custom apps urls
from home import urls as home_urls
from accounts import urls as accounts_urls
from visitor import urls as visitor_urls
from authority import urls as authority_urls
from employee import urls as employee_urls
from receptonist import urls as receptonist_urls
from report import urls as report_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(home_urls)),
    path("", include(accounts_urls)),
    path("", include(visitor_urls)),
    path("", include(authority_urls)),
    path("", include(employee_urls)),
    path("", include(receptonist_urls)),
    path("", include(report_urls)),
]

# for serve static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
