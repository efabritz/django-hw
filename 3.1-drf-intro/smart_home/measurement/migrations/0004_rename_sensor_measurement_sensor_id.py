# Generated by Django 4.1.3 on 2022-11-17 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("measurement", "0003_alter_measurement_sensor"),
    ]

    operations = [
        migrations.RenameField(
            model_name="measurement", old_name="sensor", new_name="sensor_id",
        ),
    ]
