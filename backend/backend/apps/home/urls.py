from django.urls import path
from home import views
urlpatterns = [
    path("get", views.TestView.as_view()),
    path("", views.get)
]