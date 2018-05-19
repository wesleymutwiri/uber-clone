from django.conf.urls import url,include
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from driver import views as core_views

urlpatterns = [
    # url(r'^$', views.index, name= 'index'),
    url(r'^driver/', views.driver, name = 'driver'),
    url(r'^signup/$', core_views.driver_signup, name='driver_signup'),
]

