# Generated by Django 4.1.1 on 2023-01-30 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0021_project_created_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="created_by",
        ),
    ]
