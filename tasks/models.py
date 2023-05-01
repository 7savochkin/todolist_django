from django.contrib.auth import get_user_model
from django.db import models
from django_lifecycle import LifecycleModelMixin, hook, AFTER_UPDATE

from base.mixins.model_mixin import PrimaryKeyMixin

User = get_user_model()


class TaskBook(PrimaryKeyMixin):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    expired_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | {self.expired_date}"


class Task(LifecycleModelMixin, PrimaryKeyMixin):
    title = models.CharField(max_length=100)
    expired_date = models.TimeField()
    is_done = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_book = models.ForeignKey(TaskBook, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | {self.task_book} | {self.expired_date}"

    @hook(AFTER_UPDATE, when='title', has_changed=True)
    def after_update_task(self):
        print(self.title, self.is_done)

    class Meta:
        ordering = ('is_done',)
