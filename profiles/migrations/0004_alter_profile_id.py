# Generated by Django 5.0.4 on 2024-04-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0003_auto_20240321_1549"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
