from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import OrderingFilter

from tracker.common.consts import NOT_AUTHORIZED_MESSAGE
from tracker.models import App
from tracker.serializers.app_serializer import AppSerializer


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'createdBy']

    def get_queryset(self):
        queryset = App.objects.all()
        name = self.request.query_params.get('name')
        description = self.request.query_params.get('description')
        createdBy = self.request.query_params.get('createdBy')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if description:
            queryset = queryset.filter(description__icontains=description)
        if createdBy:
            queryset = queryset.filter(createdBy__username=createdBy)

        return queryset

    def perform_create(self, serializer):
        serializer.save(createdBy=self.request.user)

    def update(self, request, *args, **kwargs):
        app = self.get_object()
        if not request.user.is_superuser and request.user != app.createdBy:
            raise PermissionDenied(NOT_AUTHORIZED_MESSAGE)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        app = self.get_object()
        if not request.user.is_superuser and request.user != app.createdBy:
            raise PermissionDenied(NOT_AUTHORIZED_MESSAGE)
        return super().destroy(request, *args, **kwargs)
