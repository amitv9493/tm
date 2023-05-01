from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


# Create your models here.


class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=128, blank=True)
    warehouse_location = models.CharField(max_length=128, blank=True)
    warehouse_contact = PhoneNumberField(max_length=128, blank=True)
    warehouse_email = models.EmailField(max_length=128, blank=True)
    warehouse_manager = models.CharField(max_length=128, blank=True)
    # warehouse_equipments=models.ManyToManyField("Equipment",related_name="warehouse_equipments",default="")
    # warehouse_parts=models.ManyToManyField("Part",related_name="warehouse_parts",default="")
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    country = CountryField(null=True, blank=True)

    def __str__(self):
        return self.warehouse_name
