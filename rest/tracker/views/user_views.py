from rest_framework import generics
from rest_framework.response import Response

from tracker.serializers.user_serializer import UserRegisterSerializer, UserLoginSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({"user": UserRegisterSerializer(user).data})
