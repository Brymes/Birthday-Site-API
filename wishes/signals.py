from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from .models import Wishes

from django.core.mail import send_mail


@receiver(post_save, sender=Wishes)
def send_tribute_to_mail(sender, instance, created, **kwargs):
    if created:
        print(sender)
        print("alknfasnalk")

        mess = f"{instance.message}"
        subject = f"Birthday Tribute from {instance.name}"
        send_mail(message=mess, recipient_list=[
                  "samuel.jennifer.olowo@gmail.com", "saolowo@yahoo.com"], subject=subject, fail_silently=False)
