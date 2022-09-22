from email.mime import base
from django.urls import path, include
from rest_framework import routers
from .views import UserSignUpView, UserSignInView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = routers.DefaultRouter()

urlpatterns =[
    path('', include(router.urls)),
    # 회원가입/로그인
    path("sign-up/", UserSignUpView.as_view()),
    path("sign-in/", UserSignInView.as_view()),
    # 토큰
    path("token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh", TokenRefreshView.as_view(), name='token_refresh'),
    path("token/verify", TokenVerifyView.as_view(), name='token_verify'),
]