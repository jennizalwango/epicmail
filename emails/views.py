from rest_framework import generics
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class ListUserView(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def get_queryset(self):
    fname = self.kwargs.get('firstname', None)
    if fname:
      return User.objects.filter(first_name__iexact = fname)
    else:
      return User.objects.all()
