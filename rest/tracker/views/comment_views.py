from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from tracker.common.consts import NOT_AUTHORIZED_MESSAGE
from tracker.models import Comment
from tracker.serializers.comment_serializer import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'created_at', 'createdBy']

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


class EntryCommentsView(ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        entry_id = self.kwargs.get('entry_id')
        return Comment.objects.filter(entry_id=entry_id).order_by('createdAt')
