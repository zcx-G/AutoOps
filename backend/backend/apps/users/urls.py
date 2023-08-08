from django.urls import path
from host import views
urlpatterns = [
    path("get", views.HostView.as_view()),
]