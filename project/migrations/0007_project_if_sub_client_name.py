# Generated by Django 4.1.1 on 2022-11-16 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_project_scope_of_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='if_sub_client_name',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
