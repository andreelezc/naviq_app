# Generated by Django 4.2.5 on 2023-10-04 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("evaluation", "0002_criterion_delete_criteria_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="property", options={"verbose_name_plural": "properties"},
        ),
    ]
