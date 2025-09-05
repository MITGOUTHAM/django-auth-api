import random
from django.contrib.auth import get_user_model, authenticate
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from .serializers import (
    RegisterSerializer,
    VerifyOTPSerializer,
    LoginSerializer,
    UserSerializer,
    LogoutSerializer,
)

User = get_user_model()


# ------------------ REGISTER ------------------
class RegisterView(APIView):
    permission_classes = [AllowAny]  # Public endpoint

    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        if User.objects.filter(email=email).exists():
            return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

        otp = str(random.randint(100000, 999999))
        user = User.objects.create_user(email=email, password=password, is_active=False)
        user.otp = otp
        user.save()

        # Print OTP to console for testing
        print(f"OTP for {email}: {otp}")

        return Response(
            {"message": "User registered. Please verify OTP (check console)."},
            status=status.HTTP_201_CREATED
        )


# ------------------ VERIFY OTP ------------------
class VerifyOTPView(APIView):
    permission_classes = [AllowAny]  # Public endpoint

    @swagger_auto_schema(request_body=VerifyOTPSerializer)
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        otp = serializer.validated_data["otp"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        if user.is_active:
            return Response({"message": "User is already verified"}, status=status.HTTP_200_OK)

        if user.otp != otp:
            return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.otp = None  # clear OTP after verification
        user.save()

        return Response({"message": "User verified successfully"}, status=status.HTTP_200_OK)


# ------------------ LOGIN ------------------
class LoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, email=email, password=password)
        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        if not user.is_active:
            return Response({"error": "User not verified"}, status=status.HTTP_403_FORBIDDEN)

        # Optional: Track login
        # from .models import LoginHistory
        # LoginHistory.objects.get_or_create(user=user)  # only one record per user

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response = Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        response.set_cookie(
            key="auth_token",
            value=access_token,
            httponly=True,
            secure=False,
            samesite="Lax",
        )
        return response



# ------------------ COOKIE JWT AUTH ------------------
class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        raw_token = request.COOKIES.get("auth_token")
        if raw_token is None:
            return None
        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token



# ------------------ USER DETAILS ------------------
class UserDetailsView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            "id": user.id,
            "email": user.email,
            "is_active": user.is_active,
        }
        return Response(data, status=status.HTTP_200_OK)




# ------------------ LOGOUT ------------------
class LogoutView(APIView):
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email", None)

        response = Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        response.delete_cookie("auth_token")
        return response
