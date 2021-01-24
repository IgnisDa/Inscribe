from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.CustomUserCreateView.as_view(), name="register"),
    path("info/<int:pk>/", views.CustomUserDetailView.as_view(), name="info"),
    path("discover/", views.CustomUserCreateView.as_view(), name="discover"),
]
