from django.shortcuts import render
from .models import Project
from .serializers import DashboardSerializer
from rest_framework import generics 
import pytz
from datetime import datetime 
from tm_api.paginator import CustomPagination

def projectview(request,pk):
    context ={
        'obj':Project.objects.get(id=pk)
    }
    return render(request,'comments.html', context = context)


class DashboardView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = DashboardSerializer
    pagination_class = CustomPagination
    current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()
    def get_queryset(self):
        print(self.current_datetime)
        
        qs =  super().get_queryset()
        status = (self.request.GET.get("status"))

        if status =='0': # ongoing
            qs = qs.filter(project_start__lte = self.current_datetime, project_end__gte = self.current_datetime, )

        if status =='1':
            qs = qs.filter(project_start__gte = self.current_datetime)
            
        return qs