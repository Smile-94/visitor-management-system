from django.db.models.signals import post_save
from django.dispatch import receiver

#models
from accounts.models import User
from visitor.models import VisitorInfo
from visitor.models import VisitorMediaLink

@receiver(post_save, sender=User)
def create_visitor_profile(sender, instance, created, *args, **kwargs):
    if created and instance.is_visitor==True:
        VisitorInfo.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, *args, **kwargs):
    if instance.is_visitor==True:
        instance.visitor_info.save()


@receiver(post_save, sender=User)
def create_visitor_media_link(sender, instance, created, *args, **kwargs):
    if created and instance.is_visitor==True:
        VisitorMediaLink.objects.create(link_of=instance)


@receiver(post_save, sender=User)
def save_media_link(sender, instance, *args, **kwargs):
    if instance.is_visitor==True:
        instance.visitor_link.save()