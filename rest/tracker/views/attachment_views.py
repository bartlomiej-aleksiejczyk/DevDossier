from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import OrderingFilter

from tracker.common.consts import NOT_AUTHORIZED_MESSAGE
from tracker.models import App
from tracker.serializers.app_serializer import AppSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

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
