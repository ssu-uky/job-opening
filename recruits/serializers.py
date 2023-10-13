from .models import Recruit
from rest_framework import serializers


class RecruitSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Recruit
        fields = (
            "id",
            "company_name",
            "title",
            "position",
            "reward",
            "skill",
            "content",
        )
        read_only_fields = ("pk",)
    
    def get_company_name(self, obj):
        return obj.company.company_name
