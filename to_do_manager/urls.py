from django.contrib import admin
from django.urls import path, include

from .views import TaskListView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tag/", TaskListView.as_view(), name="tag-list"),
]


app_name = "to_do_manager"
