from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied

from tracker.common.consts import NOT_AUTHORIZED_MESSAGE
from tracker.models import Attachment
from tracker.serializers.attachment_serializer import AttachmentSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def update(self, request, *args, **kwargs):
        attachment = self.get_object()
        if not request.user.is_superuser and request.user != attachment.createdBy:
            raise PermissionDenied(NOT_AUTHORIZED_MESSAGE)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        attachment = self.get_object()
        if not request.user.is_superuser and request.user != attachment.createdBy:
            raise PermissionDenied(NOT_AUTHORIZED_MESSAGE)
        return super().destroy(request, *args, **kwargs)
