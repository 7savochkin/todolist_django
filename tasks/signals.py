from django.db.models.signals import pre_save
from django.dispatch import receiver
from tasks.models import TaskBook


@receiver(pre_save, sender=TaskBook)
def pre_save_task_book(sender, **kwargs):
    print(f"PRE SAVE SIGNAL {sender} {kwargs}")
