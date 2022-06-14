from django.urls import path

from home.views import HomeIndexTemplateView

app_name = 'home'
urlpatterns = [
    path('', HomeIndexTemplateView.as_view(), name='index')
]
