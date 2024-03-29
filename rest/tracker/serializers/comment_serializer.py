from rest_framework import serializers

from tracker.models import Comment, Attachment
from tracker.serializers.attachment_serializer import AttachmentSerializer


class CommentSerializer(serializers.ModelSerializer):
    attachment = AttachmentSerializer(allow_null=True, required=False)

    class Meta:
        model = Comment
        fields = ['body', 'attachment', 'createdBy', 'entry']
        read_only_fields = ['createdBy']

    def __init__(self, *args, **kwargs):
        super(CommentSerializer, self).__init__(*args, **kwargs)

        if self.context['request'].method in ['PUT', 'PATCH']:
            self.fields['attachment'].read_only = True

    def create(self, validated_data):
        attachment_data = validated_data.pop('attachment', None)
        comment = Comment.objects.create(**validated_data)

        if attachment_data:
            attachment_data['createdBy'] = validated_data['createdBy']
            attachment = Attachment.objects.create(comment=comment, **attachment_data)
            comment.attachment_id = attachment.id
            comment.save()

        return comment
