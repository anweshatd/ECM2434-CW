# Generated by Django 5.0.2 on 2024-03-19 15:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="badges",
            field=models.CharField(default=0, max_length=50),
        ),
    ]
