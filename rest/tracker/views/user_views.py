from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from tracker.serializers.user_serializer import UserRegisterSerializer, UserLoginSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        response = Response(dict(
            success=True,
            message="Login successful",
            data=UserRegisterSerializer(user).data
        ))
        response.set_cookie(
            key='auth_token',
            value=token.key,
            httponly=True,
            secure=False,
            samesite='Lax'
        )
        return response


class UserLogoutView(APIView):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            response = Response({
                "success": True,
                "message": "Logout successful",
            })
            response.delete_cookie('auth_token')
            return response
        else:
            return Response({
                "success": False,
                "message": "You are not logged in",
            }, status=status.HTTP_400_BAD_REQUEST)
