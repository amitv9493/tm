# Generated by Django 4.1.1 on 2022-12-12 09:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0115_reactor_select_tube_protude_bottom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='alternate_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Alternate Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='comman_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Comman Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='contact_person',
            field=models.CharField(blank=True, max_length=128, verbose_name='Contact Person'),
        ),
        migrations.AlterField(
            model_name='client',
            name='contact_person_email',
            field=models.EmailField(blank=True, max_length=128, verbose_name='Contact Person Email'),
        ),
        migrations.AlterField(
            model_name='client',
            name='contact_person_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Contact Person Phone'),
        ),
        migrations.AlterField(
            model_name='client',
            name='former_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Former Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='official_address',
            field=models.ManyToManyField(related_name='official_address', to='client.address', verbose_name='Official Adrress'),
        ),
        migrations.AlterField(
            model_name='client',
            name='parent_company',
            field=models.CharField(blank=True, max_length=128, verbose_name='Parent Company'),
        ),
        migrations.AlterField(
            model_name='client',
            name='plantentrance_address',
            field=models.ManyToManyField(related_name='plantentrance_address', to='client.address', verbose_name='Plant Entrance Address'),
        ),
        migrations.AlterField(
            model_name='client',
            name='shipping_address',
            field=models.ManyToManyField(related_name='shipping_address', to='client.address', verbose_name='Shipping Address'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='plant_contact',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Plant Contact'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='plant_location',
            field=models.CharField(blank=True, max_length=128, verbose_name='Plant Location'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='is_there_ferrule_insert_in_tube',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=128, verbose_name='Is There Ferrule Insert In Tube?'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='reactor_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Reactor Name'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='top_tube_sheet_thickness',
            field=models.CharField(choices=[('INCH', 'INCH'), ('MM', 'MM')], max_length=128, verbose_name='Top Tube Sheet Thickness'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='chemical_being_manufactured_by_this_unit',
            field=models.CharField(blank=True, max_length=128, verbose_name='Chemical Being Manufactured By This Unit'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name_of_unit',
            field=models.CharField(blank=True, max_length=128, verbose_name='Name Of Unit'),
        ),
    ]
