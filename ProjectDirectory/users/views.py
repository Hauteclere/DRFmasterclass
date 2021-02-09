from .models import CustomUser
from .serializers import UserSerializer, UserDetailSerializer, TeamSelectionSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user

class AddTeam(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = TeamSelectionSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)