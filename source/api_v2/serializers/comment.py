from rest_framework import serializers
from webapp.models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'article', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'article', 'created_at', 'updated_at']

    def validate_content(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Комментарий не может быть пустым.")
        return value
