from .models import Recruit
from rest_framework import serializers


class RecruitSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()
    
    class Meta:
        model = Recruit
        fields = (
            "id",
            "company",
            "title",
            "position",
            "reward",
            "skill",
            "content",
        )
        read_only_fields = ("id",)

    def get_company(self, obj):
        return obj.company.company_name


class RecruitListSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()
    
    class Meta:
        model = Recruit
        fields = (
            "id",
            "company",
            "title",
            "position",
            "reward",
            "skill",
            "content",
        )
        read_only_fields = ("id",)
    
    def get_company(self, obj):
        return obj.company.company_name
