from rest_framework import serializers
from .models import UserSession

class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ['id', 'user', 'session_key', 'ip_address', 'user_agent', 'created_at', 'is_active']