from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, LogoutSerializer


class RegisterApiView(APIView):
    permission_classes = [AllowAny]
    serializers_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Qeydiyyat ugurla tamamlandi!"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class LogoutApiView(APIView):
    permission_classes = [IsAuthenticated]
    serializers_class = LogoutSerializer

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "Sistem ugurla cixis etdiniz!"},
                status=status.HTTP_205_RESET_CONTENT,
            )

        except Exception:
            return Response(
                {"error": "Yanlis token formati!"}, status=status.HTTP_400_BAD_REQUEST
            )
