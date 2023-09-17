# Generated by Django 4.2.4 on 2023-09-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cars",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("care_name", models.CharField(max_length=100)),
                ("car_version", models.CharField(max_length=3)),
                ("car_model", models.CharField(max_length=30)),
            ],
        ),
    ]
