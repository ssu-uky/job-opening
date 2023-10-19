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
    created_at = models.DateTimeField(auto_now_add=True)
    recruit_user = models.ManyToManyField(
        "users.User",
        blank=True,
        verbose_name="지원한 사람",
        related_name="recruited_user",
    )

    def __str__(self):
        return self.title
