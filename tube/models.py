from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.core.exceptions import ValidationError


# Create your models here.
def slugFieldValidator(value):
    if slugify(value) in Warehouse.objects.all().values_list("slug", flat=True):
        raise ValidationError("please input a unique name")
    return value


class Warehouse(models.Model):
    warehouse_name = models.CharField(
        max_length=128, blank=True, validators=[slugFieldValidator], unique=True
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
