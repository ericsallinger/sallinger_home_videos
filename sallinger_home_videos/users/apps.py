from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "sallinger_home_videos.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import sallinger_home_videos.users.signals  # noqa F401
        except ImportError:
            pass
