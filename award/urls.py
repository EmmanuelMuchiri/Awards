from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns=[
    url(r'^$',views.index,name='Projects'),
    url(r'^user/(?P<username>\w{0,50})',views.profile,name='profile'),
    url(r'^create/profile$',views.create_profile, name='new-profile'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^project/(\d+)',views.project,name ='project'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^project_site/(\d+)',views.project_site,name='project_site'),
# API EndPoints URL for Profile and Projects which people can consume

    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectList.as_view())

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)