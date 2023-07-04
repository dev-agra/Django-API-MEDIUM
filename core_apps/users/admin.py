from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import UserChangeForm, UserCreationForm
from .models import User

class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    
    list_display = ["pkid", "id", "email", "first_name", "last_name", "is_staff", "is_active"]
    
    list_display_links = ["pkid", "id", "email"]
    
    list_filter = [
        "email", "is_staff", "is_active"
    ]
    
    # standard model admin attributes
    fieldsets = (
        (_("Login Credentials"), {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name")}),
        (_("Permissions and Groups"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    # User model overrides the get fieldsets to use this attribute when creating a user
    add_fieldsets = (
        None, 
        {
            # causes the fieldsets to use the full width of the change form
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password1", "password2"),
        },
    )
    # admin to be able to search with email, first_name, last_name
    search_fields = ["email", "first_name", "last_name"]
    

admin.site.register(User, UserAdmin)

    