from django.db import models


# Create your models here.
class Company(models.Model):
    """회사 모델"""

    company_name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name
