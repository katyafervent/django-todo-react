
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from todo import views

schema_view = get_swagger_view(title='API docs')

router = routers.DefaultRouter()
router.register('todos', views.TodoViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view),
    path('', include(router.urls))
]

