# Generated by Django 4.1.2 on 2022-10-28 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0004_alter_article_scopes"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article", old_name="scopes", new_name="tag",
        ),
    ]
