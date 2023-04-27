from django.contrib import admin

from tasks.models import TaskBook, Task


@admin.register(TaskBook)
class TaskBookAdmin(admin.ModelAdmin):
    ...


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ...
