from .models import Company
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            "id",
            "company_name",
            "address",
            "country",
            "city",
        )

    read_only_fields = ("id",)
