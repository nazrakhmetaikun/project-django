from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Products
from django.core.mail import send_mail

@receiver(post_save,sender=Products)
def send_notify_product(instance,created):
    if created:
        send_mail(subject=f"{instance.store.user.email} you product {instance.name} added to store.", recipient_list=[instance.store.user.email])