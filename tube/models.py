from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from project.validators import slugFieldValidator
from django.utils.text import slugify


class Warehouse(models.Model):
    warehouse_name = models.CharField(
        max_length=128,
        blank=True,
    )
    warehouse_location = models.CharField(max_length=128, blank=True)
    warehouse_contact = models.CharField(max_length=128, blank=True)
    warehouse_email = models.EmailField(max_length=128, blank=True)
    warehouse_manager = models.CharField(max_length=128, blank=True)
    slug = models.SlugField(max_length=500, null=True, blank=True)
    # warehouse_equipments=models.ManyToManyField("Equipment",related_name="warehouse_equipments",default="")
    # warehouse_parts=models.ManyToManyField("Part",related_name="warehouse_parts",default="")
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    country = CountryField(null=True, blank=True)

    def __str__(self):
        return self.warehouse_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.warehouse_name)
        print(self.slug)
        return super(Warehouse, self).save(*args, **kwargs)

    def clean_warehouse_name(self):
        value = self.warehouse_name
        id = self.id
        qs = Warehouse.objects.all()
        slugFieldValidator(value, qs, id)

    def clean(self):
        super().clean()  # Call the parent's clean() method

        self.clean_warehouse_name()
