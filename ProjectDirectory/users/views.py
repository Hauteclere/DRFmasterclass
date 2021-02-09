from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
