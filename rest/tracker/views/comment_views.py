from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tracker.forms.comment_forms import CommentForm
from tracker.models import Entry, Attachment


class CommentViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_comments(self, request, pk=None):
        return Response(
            dict(
                success=True,
                message=(board_instance and "apiColumnUpdated" or "apiColumnAdded"),
                data=BoardSerializer(Board.objects.all(), many=True).data
            )
        )
