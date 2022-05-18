from rest_framework import serializers
from api_basic.models import Employeemodel

class Employeeserialize(serializers.ModelSerializer):
    class Meta:
        model = Employeemodel
        fields = "__all__"


