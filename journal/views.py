from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from journal.models import Journal
from journal.serializers import JournalSerializer


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('child__is_studying',)

