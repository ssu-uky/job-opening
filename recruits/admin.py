from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Recruit)
class RecruitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company",
        "title",
        "position",
        "reward",
        "skill",
    )
    list_display_links = (
        "id",
        "company",
        "title",
    )
    list_filter = (
        "company",
        "position",
        "skill",
    )
    search_fields = (
        "company",
        "position",
        "reward",
        "skill",
    )
