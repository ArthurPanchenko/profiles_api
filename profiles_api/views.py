from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from .serializers import UserProfileSerializer
from .permissions import UpdateOwnProfile
from .models import UserProfile


class UserProfileViewSet(ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [UpdateOwnProfile,]
    