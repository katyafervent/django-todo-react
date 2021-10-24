from rest_framework import serializers

from .models import Category, TodoItem


class TodoModelSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = TodoItem
        fields = (
            'id',
            'title',
            'description',
            'completed',
            'due_date',
            'category'
        )

    def create(self, validated_data):
        category = validated_data.get('category')
        if category:
            category = Category.objects.get_or_create(**category)

        todoItem = TodoItem.objects.create(**validated_data)
        return todoItem

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
