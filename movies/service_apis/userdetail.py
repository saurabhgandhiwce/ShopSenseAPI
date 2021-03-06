from django.contrib.auth.models import User
from rest_framework import generics

from movies.utils.serializers import UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
