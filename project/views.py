from django.shortcuts import redirect, render
from .models import Project
from .serializers import DashboardSerializer
from rest_framework import generics
import pytz
from datetime import datetime
from tm_api.paginator import CustomPagination
from django.utils import timezone

def projectview(request, pk):
    context = {"obj": Project.objects.get(id=pk)}
    return render(request, "comments.html", context=context)


class DashboardView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = DashboardSerializer
    pagination_class = CustomPagination
    current_datetime = timezone.now().date()

    def get_queryset(self):
        print(self.current_datetime)

        qs = super().get_queryset()
        status = self.request.GET.get("status", None)

        if status == "0":  # ongoing
            qs = qs.filter(
                project_start__lte=self.current_datetime,
                project_end__gte=self.current_datetime,
            )

        if status == "1":
            qs = qs.filter(project_start__gte=self.current_datetime)

        return qs


def my_custom_page_not_found_view(request, exception):
    x = request.path
    return redirect("front")
