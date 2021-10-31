from rest_framework import serializers

from .models import Category, TodoItem


class SerializerMethodField(serializers.ModelSerializer):
    def get_category(self, obj):
        return obj.category.values_list('name', flat=True)

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name') 


class CategoryField(serializers.Field):

    def to_internal_value(self, name):
        return name

    def to_representation(self, obj):
        return obj.name

class TodoModelSerializer(serializers.ModelSerializer):
    category = CategoryField(required=False)

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
            category, is_created = Category.objects.get_or_create(name=category)
        validated_data['category'] = category
        todoItem = TodoItem.objects.create(**validated_data)
        return todoItem
