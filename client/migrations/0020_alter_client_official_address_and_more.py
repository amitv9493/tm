# Generated by Django 4.1.1 on 2022-09-21 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0019_reactor_inch3_reactor_inch4_reactor_inch5_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='official_address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='official_address', to='client.address'),
        ),
        migrations.AlterField(
            model_name='client',
            name='plantentrance_address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plantentrance_address', to='client.address'),
        ),
        migrations.AlterField(
            model_name='client',
            name='shipping_address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='client.address'),
        ),
    ]
