from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.NewCompanyView.as_view(), name="new_company"),
    path("list/", views.CompanyListView.as_view(), name="company_list"),
    path("list/<int:pk>/", views.CompanyDetailView.as_view(), name="company_detail"),
]
