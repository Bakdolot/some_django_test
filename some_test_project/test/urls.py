from django.urls import path

from .views import MainView

urlpatterns = [path("check/", MainView.as_view())]
