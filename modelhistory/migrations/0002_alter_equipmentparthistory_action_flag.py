# Generated by Django 3.2.16 on 2023-09-18 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelhistory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentparthistory',
            name='action_flag',
            field=models.CharField(choices=[('1', 'Added'), ('0', 'Dismantled')], max_length=1),
        ),
    ]
