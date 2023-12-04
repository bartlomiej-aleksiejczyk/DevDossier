from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from tracker.common.consts import NOT_AUTHORIZED_MESSAGE
from tracker.enums.entry_enums import EntryType, EntryStatus, EntryPriority
from tracker.models import Entry
from tracker.serializers.entry_serializer import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'type', 'status', 'createdBy', 'lastUpdated', 'createdAt']

    def perform_create(self, serializer):
        serializer.save(createdBy=self.request.user)

    def update(self, request, *args, **kwargs):
        entry = self.get_object()
        if not request.user.is_superuser and request.user != entry.createdBy:
            raise PermissionDenied(NOT_AUTHORIZED_MESSAGE)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        entry = self.get_object()
        if not request.user.is_superuser and request.user != entry.createdBy:
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
        print(entry_type)
        if entry_type in EntryType.__members__:
            queryset = queryset.filter(type=EntryType[entry_type].name)

        entry_status = self.request.query_params.get('status')
        print(entry_status)
        print(EntryStatus.__members__)
        print(entry_status in EntryStatus.__members__)
        if entry_status in EntryStatus.__members__:
            print(EntryStatus[entry_status].value)
            queryset = queryset.filter(status=EntryStatus[entry_status].name)

        entry_priority = self.request.query_params.get('priority')
        print(entry_priority)
        if entry_priority in EntryPriority.__members__:
            print(EntryPriority[entry_priority].value)
            queryset = queryset.filter(priority=EntryPriority[entry_priority].name)

        return queryset.order_by('createdAt')


class UserEntriesView(ListAPIView):
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Entry.objects.filter(createdBy_id=user_id)
