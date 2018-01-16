from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from users.permissions import UserPermission
from users.serializers import UserSerializer


class UserCreateAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]