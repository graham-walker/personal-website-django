from django.urls import include, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('personal.urls')),
]
