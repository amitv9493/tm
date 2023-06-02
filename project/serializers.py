from rest_framework import serializers
from .models import Project

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        depth =1 