# Generated by Django 5.1.4 on 2025-01-09 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("miapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="image",
            field=models.ImageField(default="null", upload_to=""),
        ),
    ]
