from django.apps import AppConfig


class ModelhistoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modelhistory'

    def ready(self) -> None:
        from .import signals