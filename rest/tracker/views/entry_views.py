from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from tracker.common.consts import NOT_AUTHORIZED_MESSAGE
from tracker.enums.entry_enums import EntryType, EntryStatus, EntryPriority
from tracker.models import App, Entry
from tracker.serializers.entry_serializer import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'type', 'status', 'createdBy', 'lastUpdated', 'createdAt']

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


class AppEntriesView(ListAPIView):
    serializer_class = EntrySerializer
    pagination_class = PageNumberPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'type', 'status', 'createdBy', 'lastUpdated', 'createdAt']

    def get_queryset(self):
        app_id = self.kwargs.get('app_id')
        queryset = Entry.objects.filter(app_id=app_id)

        entry_type = self.request.query_params.get('type')
        if entry_type in EntryType.__members__:
            queryset = queryset.filter(type=EntryType[entry_type].value)

        entry_status = self.request.query_params.get('status')
        if entry_status in EntryStatus.__members__:
            queryset = queryset.filter(status=EntryStatus[entry_status].value)

        entry_priority = self.request.query_params.get('priority')
        if entry_priority in EntryPriority.__members__:
            queryset = queryset.filter(status=EntryPriority[entry_priority].value)

        return queryset.order_by('createdAt')
