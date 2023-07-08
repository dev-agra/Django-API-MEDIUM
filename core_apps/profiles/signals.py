import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
# importing the user model
from mediumapi.settings.base import AUTH_USER_MODEL
# importing the profile model
from core_apps.profiles.models import Profile

logger = logging.getLogger(__name__)

# sender triggers the signal
@receiver(post_save, sender=AUTH_USER_MODEL)
# instance refers to the specific instance of model that triggers the signal
def create_user_profile(sender, instance, created, **kwargs):
    # created is a boolean that tells if instance is created/updated
    if created:
        Profile.objects.create(user=instance)
        logger.info(f"{instance}'s a Profile has been created")