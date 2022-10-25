# Generated by Django 4.1.2 on 2022-10-24 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Phone",
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
                ("name", models.CharField(max_length=20)),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                ("image", models.CharField(max_length=500)),
                ("release_date", models.DateField(default=datetime.date.today)),
                ("lte_exists", models.BooleanField()),
                ("slug", models.CharField(max_length=5)),
            ],
        ),
    ]
