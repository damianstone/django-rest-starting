from rest_framework import serializers
from api import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.User
        exclude = ["password", "user_permissions", "groups",
                   "is_staff", "is_active", "is_superuser", "last_login"]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
