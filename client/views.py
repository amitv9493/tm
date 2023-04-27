from dal import autocomplete
from django.shortcuts import render
# from notifications.models import Notification
from django.db.models import Q

from .models import Reactor
from client.models import Unit

# class ReactorAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         # Don't forget to filter out results depending on the visitor !
#         if not self.request.user.is_authenticated:
#             return Reactor.objects.none()

#         qs = Reactor.objects.all()

#         if self.q:
#             qs = qs.filter(name__istartswith=self.q)

#         return qs
# Create your views here.

class ReactorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Reactor.objects.none()

        qs = Reactor.objects.all()
        
        a = self.forwarded.get('client', None) 
        b = self.forwarded.get('unit', None)
        
        if a and b:
            qs = qs.filter(Q(client=a) & Q(unit=b))

        if self.q:
            
            qs = None

        return qs
        
def front(request):
    context = {}
    return render(request, 'index.html', context)
    
class UnitAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Unit.objects.none()
            
        qs = Unit.objects.all()
        
        a = self.forwarded.get('client', None)
        
        if a:

            qs = qs.filter(client=a)
            
        else:
            qs = Unit.objects.none()
            
        if self.q:
            qs=None
        
        return qs
            
            
from client.models import Plant

class PlantAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Plant.objects.none()
            
        qs = Plant.objects.all()
        
        a = self.forwarded.get('client', None)
        
        if a:
            qs = qs.filter(client=a)
            
        if self.q:
            qs=None
        
        return qs

def notification(request):
    qs = Notification.objects.all()
    qs1 = qs.filter(recipient=request.user)
    qs1 = qs1.unread()
    return render(request, 'notification/notify.html', {'notifications':qs1})

