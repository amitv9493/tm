# Generated by Django 3.2.16 on 2023-09-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0049_auto_20230801_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(default=1, max_length=128, unique=True, verbose_name='Project Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scope_of_work',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]