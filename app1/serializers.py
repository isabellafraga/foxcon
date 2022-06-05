from rest_framework import serializers
from app1.models import Event, Comment, Orcamento


class CommentSerializer(serializers.ModelSerializer):
    """Comentários de um determinado evento."""

    class Meta:
        model = Comment
        fields = ["usuario", "text", "commented", "event"]

class OrcamentoSerializer(serializers.ModelSerializer):
    """Comentários de um determinado evento."""

    class Meta:
        model = Orcamento
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    """Serializador utilizado para a REST de eventos."""

    class Meta:
        model = Event
        fields = ["id", "date", "event", "priority", "text_priority", "number_of_comments", "hora"]


class EventPlusCommentsSerializer(EventSerializer):
    """Serializador utilizado para a REST de eventos
    (versão com comentários)"""

    comment_event = CommentSerializer(many=True, read_only=True)

    class Meta:
        fields = ["id", "date", "event", "text_priority", "comment_event", "hora"]
