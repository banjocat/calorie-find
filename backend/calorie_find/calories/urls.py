from django.conf.urls import url
from calories.views import CalorieView


urlpatterns = [
        url(r'^$', CalorieView.as_view())
        ]
