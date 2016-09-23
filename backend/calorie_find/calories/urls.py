from django.conf.urls import url
from calories.views import calories


urlpatterns = [
        url(r'^$', calories)
        ]
