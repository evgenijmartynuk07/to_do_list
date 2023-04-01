from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    ordering = ["-created", "is_completed"]

    def post(self, request, **kwargs):
        self.object = Task.objects.get(id=self.request.POST.get("id"))

        if self.object.is_completed:
            self.object.is_completed = 0
            self.object.save()
            return redirect("to_do_manager:task-list")
        self.object.is_completed = 1
        self.object.save()
        return redirect("to_do_manager:task-list")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do_manager:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do_manager:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to_do_manager:task-list")


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do_manager:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do_manager:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do_manager:tag-list")
