# Generated by Django 3.2.16 on 2023-07-14 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0046_auto_20230714_1401'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='project',
            unique_together={('project_name', 'slug')},
        ),
    ]
