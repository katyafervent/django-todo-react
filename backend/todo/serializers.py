from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text
from rest_framework import serializers

from .models import Category, TodoItem


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name') 


class CategorySlugRelatedField(serializers.SlugRelatedField):
    
    def to_internal_value(self, data):
        try:
            categories = self.get_queryset()
            category, is_created = categories.get_or_create(
                **{self.slug_field: data}
                )
            return category
        except ObjectDoesNotExist:
            self.fail('does_not_exist',
                      slug_name=self.slug_field,
                      value=smart_text(data)
            )
        except (TypeError, ValueError):
            self.fail('invalid')


class TodoModelSerializer(serializers.ModelSerializer):
    category = CategorySlugRelatedField(
        slug_field='name',
        required=False,
        queryset=Category.objects.all()
    )

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
