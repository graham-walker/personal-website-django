from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^posts/$', views.posts, name='posts'),
    re_path(r'^posts/(?P<pk>\d+)/?$', views.post, name='post'),
    re_path(r'^media/$', views.MediaView.as_view(), name='media'),
    re_path(r'^delete/media/(?P<pk>\d+)/?$', views.delete, name='deleteMedia'),
    re_path(r'^logout/?$', views.logoutView, name='logout'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
