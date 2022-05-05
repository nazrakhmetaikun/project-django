from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from .models import Orders

@receiver(post_save,sender=Orders)
def send_notification_about_order(instance, created,**kwargs):
    if created:
        template = f"Hello, {instance.user.get_full_name()}! Your order {instance.uuid} created."
        send_mail(subject=template,recipient_list=[instance.user.email])
        store_list = [ item.product.store.user for item in instance.items.all()]
        for user in store_list:
            template = f"Hello, {user.get_full_name()}! You get new order {instance.uuid}."
            send_mail(subject=template,recipient_list=[user.email])



@receiver(post_save,sender=Orders)
def send_notification_about_order(instance, created,**kwargs):
    if instance.canceled:
        template = f"Hello, {instance.user.get_full_name()}! Your order {instance.uuid} canceled."
        send_mail(subject=template,recipient_list=[instance.user.email])
