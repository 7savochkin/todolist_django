from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from base.mixins.view_mixin import RequestFormViewMixin

from tasks.forms import CreateTaskBookForm
from tasks.models import TaskBook


class TaskBookList(LoginRequiredMixin, ListView):
    template_name = 'menu/task_book_list.html'
    model = TaskBook
    context_object_name = 'task_books'
    ordering = ('-updated_at',)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TaskBookDetail(LoginRequiredMixin, DetailView):
    template_name = 'menu/task_book_detail.html'
    model = TaskBook
    context_object_name = 'task_book'


class TaskBookCreate(LoginRequiredMixin, RequestFormViewMixin):
    template_name = 'menu/task_book_create.html'
    form_class = CreateTaskBookForm
    success_url = reverse_lazy('menu')
