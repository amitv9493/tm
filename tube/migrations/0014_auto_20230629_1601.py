# Generated by Django 3.2.16 on 2023-06-29 10:31

from django.db import migrations, models
import tube.models


class Migration(migrations.Migration):
    dependencies = [
        ("tube", "0013_alter_warehouse_warehouse_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="warehouse",
            name="slug",
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="warehouse",
            name="warehouse_name",
            field=models.CharField(
                blank=True, max_length=128, validators=[tube.models.slugFieldValidator]
            ),
        ),
    ]
