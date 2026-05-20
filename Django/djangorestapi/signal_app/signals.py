from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BlogSignal

@receiver(post_save, sender=BlogSignal)
def send_notification(sender, instance, created, **kwargs):
    if created:
        print("Notofication: Blog Created Sucessfully")