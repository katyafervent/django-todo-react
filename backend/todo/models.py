from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category,
                                 blank=True,
                                 null=True,
                                 on_delete=models.PROTECT
                                )

    def __str__(self):
        return self.title
