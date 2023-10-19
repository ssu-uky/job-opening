from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.NewUserView.as_view(), name="new_user"),
    path("list/", views.UserListView.as_view(), name="user_list"),
    path("list/<int:user_id>/", views.UserRecruitView.as_view(), name="user_recruit"),
]
