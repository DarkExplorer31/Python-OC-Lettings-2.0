# Generated by Django 3.0 on 2024-03-17 12:19
import logging
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import migrations, models


def copy_data_from_source_to_target(apps, schema_editor):
    logger = logging.getLogger(__name__)
    try:
        SourceAddress = apps.get_model("oc_lettings_site", "Address")
        TargetAddress = apps.get_model("lettings", "Address")
        for item in SourceAddress.objects.all():
            TargetAddress.objects.create(
                number=item.number,
                street=item.street,
                city=item.city,
                state=item.state,
                zip_code=item.zip_code,
                country_iso_code=item.country_iso_code,
            )
    except LookupError as e:
        logger.error(
            f"{e} - The Database has failed to import before data, now, the db is empty for address objects."
        )

    try:
        SourceLetting = apps.get_model("oc_lettings_site", "Letting")
        TargetLetting = apps.get_model("lettings", "Letting")
        for item in SourceLetting.objects.all():
            TargetLetting.objects.create(title=item.title, address_id=item.address_id)
    except LookupError as e:
        logger.error(
            f"{e} - The Database has failed to import before data, now, the db is empty for letting objects."
        )


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(copy_data_from_source_to_target),
    ]
