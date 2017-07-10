# URLS for the APP
from django.conf.urls import url
from basic_app import views

# Setting up Namespace for TEMPLATE TAGGING, this is global
app_name = "basic_app"

urlpatterns = [
    url(r"^relative/$", views.relative, name='relative'),
    url(r"^other/$", views.other, name="other"),
]
