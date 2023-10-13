from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company_name",
        "address",
        "country",
        "city",
    )
    list_display_links = (
        "id",
        "company_name",
    )
    list_filter = (
        "company_name",
        "country",
        "city",
    )
    search_fields = (
        "company_name",
        "address",
        "country",
        "city",
    )
