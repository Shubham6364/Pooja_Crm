from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("layout", views.layout, name="layout"),
    path("employee_login", views.employee_login, name="employee_login"),
    path("EB_logout", views.EB_logout, name="EB_logout"),
    path("owndata", views.owndata, name="owndata"),
    path("custdel", views.custdel, name="custdel"),
    path("owndel", views.owndel, name="owndel"),
]