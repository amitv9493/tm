# Generated by Django 3.2.16 on 2023-09-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0016_alter_warehouse_warehouse_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='slug',
            field=models.SlugField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='warehouse_name',
            field=models.CharField(max_length=128),
        ),
    ]