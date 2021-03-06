from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^$', views.posts_list, name='list'),
    url(r'^logout$', 'django.contrib.auth.views.logout',  {'next_page': '/login'}, name='logout'),
    url(r'^create$', views.posts_create, name='create'),
    url(r'^(?P<id>\d+)/edit$', views.posts_update, name='update'),
    url(r'^(?P<id>\d+)/delete$', views.posts_delete, name='delete'),
    url(r'^(?P<id>\d+)/$', views.posts_detail, name='detail'),

]