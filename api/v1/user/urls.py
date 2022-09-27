# api.v1.user.urls.py

# Django
from django.urls import path, include
# DRF
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# Internal
from .views import UserSignUpView, UserSignInView, UserView, UserSignoutView

router = DefaultRouter()

urlpatterns =[
    path('', include(router.urls)),
    # 회원가입/로그인
    path("sign-up/", UserSignUpView.as_view()),
    path("sign-in/", UserSignInView.as_view()),
    path("auth/", UserView.as_view()),
    path("sign-out/", UserSignoutView.as_view()),
    # 토큰
    path("token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh", TokenRefreshView.as_view(), name='token_refresh'),
    path("token/verify", TokenVerifyView.as_view(), name='token_verify'),
]