# Imports from existing modules.
from django.apps import AppConfig

class BlogConfig(AppConfig):
    """
        This here class contains the configurations for the current application.
        Such configurations include default behaviour, application name, special restrictions, etcetera.

        The class itself extends Django's AppConfig class.

        Author: Andrei-Paul Ionescu.
    """
    default_auto_field = 'django.db.models.BigAutoField'

    # Establish the name of the application.
    name = 'blog'

    @classmethod
    def get_name(cls):
        return cls.get_name()
