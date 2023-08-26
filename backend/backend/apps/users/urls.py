from django.urls import path
from users import views
from rest_framework_simplejwt.views import TokenObtainPairView

obt = TokenObtainPairView.as_view()
urlpatterns = [

    path("login/", obt),
    # path("login/", views.LoginView.as_view())

    # path("", views.index, name="index"),
    # path("login/", views.LoginView.as_view()),
    # path("logout", views.LogoutView.as_view()),
    # path("register/", views.register, name="register"),
    # path("user/", views.user, name="user"),
    # path("user/<int:pk>/", views.user_detail, name="user_detail"),



]