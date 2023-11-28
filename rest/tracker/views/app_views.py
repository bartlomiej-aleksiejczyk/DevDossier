from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class AppViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_apps(self, request, pk=None):
        return Response(
            dict(
                success=True,
                message=(board_instance and "apiColumnUpdated" or "apiColumnAdded"),
                data=BoardSerializer(Board.objects.all(), many=True).data
            )
        )
