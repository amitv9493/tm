# Generated by Django 3.2.16 on 2023-04-27 10:51

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0127_auto_20230427_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='alternate_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='contact_person',
        ),
        migrations.RemoveField(
            model_name='client',
            name='contact_person_email',
        ),
        migrations.RemoveField(
            model_name='client',
            name='contact_person_phone',
        ),
        migrations.RemoveField(
            model_name='client',
            name='country',
        ),
        migrations.RemoveField(
            model_name='client',
            name='official_address',
        ),
        migrations.RemoveField(
            model_name='client',
            name='plantentrance_address',
        ),
        migrations.RemoveField(
            model_name='client',
            name='shipping_address',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='plant_contact',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='plant_location',
        ),
        migrations.AddField(
            model_name='plant',
            name='contact_person',
            field=models.CharField(blank=True, max_length=128, verbose_name='Contact Person'),
        ),
        migrations.AddField(
            model_name='plant',
            name='contact_person_email',
            field=models.EmailField(blank=True, max_length=128, verbose_name='Contact Person Email'),
        ),
        migrations.AddField(
            model_name='plant',
            name='contact_person_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Contact Person Phone'),
        ),
        migrations.AddField(
            model_name='plant',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='official_address',
            field=models.ManyToManyField(blank=True, related_name='official_address', to='client.Address', verbose_name='Official Adrress'),
        ),
        migrations.AddField(
            model_name='plant',
            name='plant_common_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Plant Common Name'),
        ),
        migrations.AddField(
            model_name='plant',
            name='plant_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Plant Name'),
        ),
        migrations.AddField(
            model_name='plant',
            name='plantentrance_address',
            field=models.ManyToManyField(blank=True, related_name='plantentrance_address', to='client.Address', verbose_name='Plant Entrance Address'),
        ),
        migrations.AddField(
            model_name='plant',
            name='shipping_address',
            field=models.ManyToManyField(blank=True, related_name='shipping_address', to='client.Address', verbose_name='Shipping Address'),
        ),
    ]
