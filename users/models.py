from django.db import models
from recruits.models import Recruit
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    user_recruit = models.ForeignKey(
        Recruit,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="지원한 채용공고",
        related_name="recruited_user",
    )
    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="지원한 회사",
        related_name="users"
    )

    def __str__(self):
        return self.username
