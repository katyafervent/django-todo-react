
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from todo import views

v1_router = routers.DefaultRouter()
v1_router.register('todos', views.TodoViewSet)
v1_router.register('categories', views.CategoryViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]

