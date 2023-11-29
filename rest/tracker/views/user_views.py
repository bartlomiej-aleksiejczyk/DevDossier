from rest_framework import generics, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from tracker.common.consts import NOT_AUTHORIZED_MESSAGE
from tracker.models import User
from tracker.serializers.user_serializer import UserRegisterSerializer, UserLoginSerializer, UserCRUDSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        token, _ = Token.objects.create(user=user)
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
                "message": "Nie jesteś zalogowany",
            }, status=status.HTTP_400_BAD_REQUEST)


class UserRoleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            role = 'SUPER_USER'
        else:
            role = 'REGULAR_USER'

        return Response(dict(
            success=True,
            message='Login successful',
            data={'role': role}
        ))


class UserCRUDViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCRUDSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied(NOT_AUTHORIZED_MESSAGE)
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied(NOT_AUTHORIZED_MESSAGE)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        if not request.user.is_superuser and request.user != user:
            raise PermissionDenied(NOT_AUTHORIZED_MESSAGE)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        if not request.user.is_superuser and request.user != user:
            raise PermissionDenied(NOT_AUTHORIZED_MESSAGE)
        return super().destroy(request, *args, **kwargs)
