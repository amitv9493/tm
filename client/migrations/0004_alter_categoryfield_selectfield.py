# Generated by Django 4.1.1 on 2022-09-20 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_categoryfield_delete_dropdownmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryfield',
            name='selectfield',
            field=models.IntegerField(choices=[('INCH', 'INCH'), ('MM', 'MM')], default=1),
        ),
    ]
