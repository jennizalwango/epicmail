from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import User
from .serializers import UserSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(first_name="first_name", last_name="last_name", email="email",password="password"):
      if first_name != "" and last_name !="" and email !=""and password !="":
        User.objects.create(first_name=first_name, last_name=last_name, email=email,password=password)

    def setUp(self):
        # add test data
        self.create_user("jenny", "zawal", "jenny@gmail.com", "123456")

class GetAllUsersTest(BaseViewTest):

    def test_get_all_users(self):
        """
        This test ensures that all users added in the setUp method
        exist when we make a GET request to the users/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("users_all")
        )
        # fetch the data from db
        expected = User.objects.all()
        serialized = UserSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Create your tests here.
