from django.db import models


# Create your models here.
class Recruit(models.Model):
    """채용공고 모델"""

    company = models.ForeignKey("companies.Company", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    reward = models.PositiveBigIntegerField()
    skill = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
