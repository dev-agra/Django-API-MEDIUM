from django.apps import AppConfig
# helps in translating a django site into different languages good practice
from django.utils.translation import gettext_lazy as _

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.users"
    verbose_name = _("Users")
    # verbose_name_plural =