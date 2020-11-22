from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/$', views.posts, name='posts'),
    url(r'^posts/(?P<pk>\d+)/?$', views.post, name='post'),
    url(r'^media/$', views.MediaView.as_view(), name='media'),
    url(r'^delete/media/(?P<pk>\d+)/?$', views.delete, name='deleteMedia'),
    url(r'^logout/?$', views.logoutView, name='logout'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
