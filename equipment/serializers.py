from rest_framework import serializers
from .models import TTD


##################################################################
#       TTD Serializer
##################################################################


class TTDSerializers(serializers.ModelSerializer):
    class Meta:
        model = TTD
        fields = "__all__"
        # depth = 1


