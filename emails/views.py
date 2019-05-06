from rest_framework import generics
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class ListUserView(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def list(self, request):
    queryset = self.get_queryset()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)
# Create your views here.
