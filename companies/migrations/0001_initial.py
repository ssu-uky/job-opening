# Generated by Django 4.2.6 on 2023-10-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
            ],
        ),
    ]