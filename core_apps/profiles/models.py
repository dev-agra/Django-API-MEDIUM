# models and fields that are not linked with authenticity is provided here and ones concered with auth are in User
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _ 
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from core_apps.common.models import TimeStampedModel

User = get_user_model()

class Profile(TimeStampedModel):
    class Gender(models.TextChoices):
        MALE = "M", _("Male"),
        FEMALE = "F", _("Female"),
        OTHER = "O", _("Other"),
    # one user one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+91999999999")
    about_me = models.TextField(verbose_name=_("About Me"), default="Say Something about yourself")
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=20)
    country = CountryField(verbose_name=_("Country"), default="IN", blank=False, null=False)
    city = models.CharField(verbose_name=_("City"), max_length=180, default="MU", blank=False, null=False)
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"), default='/profile_default.png')
    twitter_handle = models.CharField(verbose_name=_("Twitter Handle"), max_length=20, blank=True)
    # Many to many relation with profile instances, self means referencing itself
    # reverse relation name of following relationship
    # symmetrical false means if A follows B then B doesn't follow A
    followers = models.ManyToManyField("self", symmetrical=False, related_name="following", blank=True)
    
    def __str__(self):
        return f"{self.user.first_name}'s Profile Name"
    
    # takes in self instance and profile instance
    def follow(self, profile):
        self.followers.add(profile)
        
    def unfollow(self, profile):
        self.followers.remove(profile)
        
    def check_following(self, profile):
        # if returned empty that means the profile is not following profile passed as the argument
        return self.followers.filter(pkid=profile.pkid).exists()

