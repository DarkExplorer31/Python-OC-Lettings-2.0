# Generated by Django 3.0 on 2024-03-17 13:44

from django.db import migrations


def copy_data_from_source_to_target(apps, schema_editor):
    try:
        SourceProfile = apps.get_model("oc_lettings_site", "Profile")
        TargetProfile = apps.get_model("profiles", "Profile")
        for item in SourceProfile.objects.all():
            TargetProfile.objects.create(
                user=item.user, favorite_city=item.favorite_city
            )
    except LookupError as e:
        print(f"Error: {e}")


class Migration(migrations.Migration):

    dependencies = [("profiles", "0001_initial")]

    operations = [
        migrations.RunPython(copy_data_from_source_to_target),
    ]
