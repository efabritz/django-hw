# Generated by Django 4.1.3 on 2022-11-17 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("measurement", "0005_rename_sensor_id_measurement_sensor"),
    ]

    operations = [
        migrations.AddField(
            model_name="measurement",
            name="image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]