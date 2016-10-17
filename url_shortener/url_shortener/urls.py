from django.conf.urls import url, include
from django.contrib import admin
from app.views import UserCreateView, LinkListView, LinkCreateView, LinkView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^linklist/$', LinkListView.as_view(), name="link_list_view"),
    url(r'^newlink$', LinkCreateView.as_view(), name="link_create_view"),
    url(r'^pass/(?P<short_url>\w+)$', LinkView.as_view(), name="pass_through_view")

]
