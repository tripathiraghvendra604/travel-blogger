from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^home$', views.home, name='home'),
    url(r'^logout$', 'django.contrib.auth.views.logout',  {'next_page': '/login'}, name='logout'),
]