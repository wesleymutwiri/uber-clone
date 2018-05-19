from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'passenger/', views.passenger, name= 'passenger'),
    url(r'^passenger/signup/$', views.passenger_signup, name='passenger_signup'),
    url(r'^passenger/login/$', views.passenger_login, name='passenger_login'),
]   