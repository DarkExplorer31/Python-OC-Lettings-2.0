# Generated by Django 3.0 on 2024-03-21 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_auto_20240317_1319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='letting',
            options={'verbose_name_plural': 'Lettings'},
        ),
    ]
