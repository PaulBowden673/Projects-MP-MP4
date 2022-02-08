from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'


class SocialAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'social_account'
