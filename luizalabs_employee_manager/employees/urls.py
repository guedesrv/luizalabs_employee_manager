from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'employees'

urlpatterns = [
    url(r'^$', views.EmployeeList.as_view(), name='list-create'),
    url(r'^(?P<pk>\d+)/$', views.EmployeeDetail.as_view(), name='delete'),
]