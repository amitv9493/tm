# Generated by Django 4.1.1 on 2022-10-20 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0003_alter_part_part_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='part_image',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
