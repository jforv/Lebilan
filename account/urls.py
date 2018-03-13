from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^accounts/$', views.account_list),
    url(r'^accounts/(?P<pk>[0-9]+)/$', views.account_detail),
]