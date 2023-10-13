from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/company/", include("companies.urls")),
    path("api/recruit/", include("recruits.urls")),
]
