from rest_framework import viewsets
from child.models import Child
from child.serializers import ChildSerializer


class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

