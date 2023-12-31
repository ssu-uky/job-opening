# Generated by Django 4.2.6 on 2023-10-19 16:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recruits', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='recruit_user',
            field=models.ManyToManyField(blank=True, related_name='recruited_user', to=settings.AUTH_USER_MODEL, verbose_name='지원한 사람'),
        ),
    ]
