from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns(
    '',
    url(r'^GET/(?P<subject>[a-zA-Z0-9_.-]+)/(?P<goal>[a-zA-Z0-9_.-]+)$', views.TeacherRequest.as_view(), name = 'TeacherRequest'),
)