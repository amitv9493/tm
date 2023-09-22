from project.models import Project
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
        
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        
        # Code to be executed for each request/response after
        # the view is called.

        return response