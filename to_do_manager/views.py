from django.shortcuts import render
from django.views import generic

from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tag")
    ordering = ["created", "is_completed"]


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"


class TaskDeleteView(generic.DeleteView):
    model = Task


class TagListView(generic.ListView):
    model = Tag
