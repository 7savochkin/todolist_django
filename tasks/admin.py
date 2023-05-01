from django.contrib import admin

from tasks.models import TaskBook, Task
from django.utils.translation import gettext_lazy as _


@admin.register(TaskBook)
class TaskBookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'user', 'created_at', 'expired_date'
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'task_book', 'is_done', 'created_at', 'expired_date'
    )
