# Generated by Django 4.1.2 on 2022-10-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0003_rename_tags_article_scopes_scope_is_main"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="scopes",
            field=models.ManyToManyField(
                related_name="scopes", through="articles.Scope", to="articles.tag"
            ),
        ),
    ]
