from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.NewCompanyView.as_view(), name="new_company"),
]
