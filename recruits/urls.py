from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.NewRecruitView.as_view(), name="new_recruit"),
    path("list/", views.RecruitListView.as_view(), name="recruit_list"),
    path("list/<int:pk>/", views.RecruitDetailView.as_view(), name="recruit_detail"),
]
