from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from tracker.forms.tag_forms import TagForm
from tracker.models import Tag


class TagViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_tags(self, request, pk=None):
        return Response(
            dict(
                success=True,
                message=(board_instance and "apiColumnUpdated" or "apiColumnAdded"),
                data=BoardSerializer(Board.objects.all(), many=True).data
            )
        )
