# we define custom user model here which is basically an 
# interface thru which db query operations are provided to Django models

from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _ 

class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email()
            return True
        except ValidationError:
            raise ValidationError(_("Users must provide a valid email address"))
        
    def create_user(self, first_name, last_name, email, password, **extra_fields):
        if not first_name:
            raise ValidationError(_("Users must have a first name."))
        if not last_name:
            raise ValidationError(_("Users must have a last name."))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValidationError(_("Users must have a email address"))
        
        user = self.model(first_name=first_name, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        
        # 
        user.save(using=self._db)
        return user
    
    def create_user(self, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)  
        extra_fields.setdefault("is_active", True)
             
        if extra_fields.get("is_staff") is not True:
            raise ValidationError(_("Superuser credentials not valid"))
        
        if extra_fields.get("is_superuser") is not True:
            raise ValidationError(_("Superuser credentials not valid"))
        
        if extra_fields.get("is_active") is not True:
            raise ValidationError(_("Superuser credentials not valid"))
        
        if not password:
            raise ValidationError(_("Superuser must have password"))
        
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValidationError(_("Superuser must have a email address"))
        user = self.create_user(first_name, last_name, email, password)
        user.save(using=self.db)
        return user