from django.conf.urls import url
from django.contrib import admin

from .views import blog_post
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/$', blog_post),
]

