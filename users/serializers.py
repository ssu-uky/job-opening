from .models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers

from recruits.models import Recruit
from companies.models import Company


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "user_recruit",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class UserRecruitSerializer(serializers.ModelSerializer):
    user_recruit = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "user_recruit",
            # "company",
        )
        read_only_fields = (
            "id",
            "password",
        )

    def get_user_recruit(self, obj):
        if obj.user_recruit:
            recruit = obj.user_recruit
            return {
                "recruit_id": recruit.id,
                "company": recruit.company.company_name,
                "title": recruit.title,
            }
        return None
