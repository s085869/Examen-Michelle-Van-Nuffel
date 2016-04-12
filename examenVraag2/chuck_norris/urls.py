from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show, name='index'),
	#url(r'^(random?P<firstName>[A-z .-]&P<lastName>[A-z .-])/$', views.show, name='show'),
]