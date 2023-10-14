from .models import Recruit
from rest_framework import serializers

from companies.serializers import CompanyRecruitSerializer


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
    # company = CompanyRecruitSerializer()
    company = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()

    class Meta:
        model = Recruit
        fields = (
            "id",
            "company",
            "country",
            "city",
            "title",
            "position",
            "reward",
            "skill",
            "content",
        )
        read_only_fields = ("id",)

    def get_company(self, obj):
        return obj.company.company_name
    
    def get_country(self, obj):
        return obj.company.country
    
    def get_city(self, obj):
        return obj.company.city
