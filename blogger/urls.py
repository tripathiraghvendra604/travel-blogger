from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^$', views.posts_list, name='list'),
    url(r'^logout$', 'django.contrib.auth.views.logout',  {'next_page': '/login'}, name='logout'),
    url(r'^create$', views.posts_create, name='create'),
    url(r'^update$', views.posts_update, name='update'),
    url(r'^delete$', views.posts_delete, name='delete'),
    url(r'^detail$', views.posts_detail, name='detail'),

]