from django.contrib import admin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

    list_display = (
        "id",
        "username",
        "password",
    )
    list_display_links = (
        "id",
        "username",
    )
    readonly_fields = (
        "id",
        "password",
    )
