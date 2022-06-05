from rest_framework import viewsets

from app1.models import Event, Comment, Orcamento
from app1.serializers import CommentSerializer, EventSerializer, OrcamentoSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CommetViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class OrcamentoViewSet(viewsets.ModelViewSet):
    queryset = Orcamento.objetos.all()
    serializer_class = OrcamentoSerializer
