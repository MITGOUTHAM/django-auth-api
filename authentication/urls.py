from django.urls import path
from .views import RegisterView, VerifyOTPView, LoginView, UserDetailsView, LogoutView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("verify-otp/", VerifyOTPView.as_view(), name="verify-otp"),
    path("login/", LoginView.as_view(), name="login"),
    path("me/", UserDetailsView.as_view(), name="me"),   # was UserDetailsView
    path("logout/", LogoutView.as_view(), name="logout"),
]
