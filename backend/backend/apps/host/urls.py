from django.urls import path
from host import views
urlpatterns = [
    path("", views.HostView.as_view()),

]