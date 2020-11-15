from rest_framework.generics import CreateAPIView
from api.serializers import UserSerializer


class RegistrationAPIView(CreateAPIView):
    serializer_class = UserSerializer
