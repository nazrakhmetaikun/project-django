from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail


@receiver(post_save,sender=User)
def send_welcome_mail(instance,created,**kwargs):
    if created:
        send_mail(subject=f"Welcome, {instance.get_full_name()}. You've registered on the website store.kz", recipient_list=[instance.email])