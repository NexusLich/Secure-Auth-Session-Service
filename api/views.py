from rest_framework import viewsets
from .models import UserSession
from .serializers import UserSessionSerializer

class UserSessionViewSet(viewsets.ModelViewSet):
    queryset = UserSession.objects.all().order_by('-created_at')
    serializer_class = UserSessionSerializer