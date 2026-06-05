from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Bu username artiq goturulub")

        return value

    def create(self, validate_data):
        return User.objects.create_user(
            username=validate_data["username"],
            email=validate_data["email"],
            password=validate_data["password"],
        )


class LogoutSerializer(serializers.ModelSerializer):
    refresh = serializers.CharField(help_text="Blackliste salinacaq refresh token.")
