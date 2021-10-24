from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, TodoItem
from .serializers import CategoryModelSerializer, TodoModelSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """Set of ToDo views with default CRUD"""
    # ToDo: get list of all undone tasks

    serializer_class = TodoModelSerializer
    queryset = TodoItem.objects.all()
    
    @action(detail=False, methods=['GET'], name='Get Uncompleted')
    def uncompleted(self, request, *args, **kwargs):
        queryset = TodoItem.objects.filter(completed=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    """Set of Category views with default CRUD"""
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
