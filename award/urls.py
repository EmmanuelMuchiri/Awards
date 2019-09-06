from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url(r'^$',views.index,name='index'),
    url(r'^user/(?P<username>\w{0,50})',views.profile,name='profile'),
    url(r'^create/profile$',views.create_profile, name='new-profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)