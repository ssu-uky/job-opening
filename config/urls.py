from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/company/", include("companies.urls")),
    path("api/recruits/", include("recruits.urls")),
    path("api/users/", include("users.urls")),
]
