from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.CreateRecruitView.as_view(), name="create_recruit"),
    path("list/", views.RecruitListView.as_view(), name="recruit_list"),
]
