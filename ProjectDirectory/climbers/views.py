from .models import Climber
from .serializers import ClimberSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsSuperuserOrReadOnly

class ClimberList(generics.ListCreateAPIView):
    queryset = Climber.objects.all()
    serializer_class = ClimberSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperuserOrReadOnly]
