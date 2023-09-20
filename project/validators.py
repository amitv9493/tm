from django.utils.text import slugify
from django.core.exceptions import ValidationError


# Create your models here.
def slugFieldValidator(value, qs, field_name=None, id=None):
    """

    Args:
        value : The value which need to be checked.
        qs : Always pass Model.objects.all()
        id (int, optional): _description_. Defaults to None.

    Raises:
        ValidationError: If the slug is already present in the database.

    Returns:
        value: Returns the value passed in the form after validating the slug is unique.

    Code Example:

        Write this in your models.py

    ```
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
    ```
    """
    if id:
        if slugify(value) in qs.exclude(id=id).values_list("slug", flat=True):
            raise ValidationError(f"please input a unique name for {field_name}")
    else:
        if slugify(value) in qs.values_list("slug", flat=True):
            raise ValidationError(f"please input a unique name for {field_name}")

    return value


def SerialValidator(self, validated_data, field_name, update: bool = False):
    from rest_framework import serializers
    
    field_value = validated_data.get(field_name, None)
    if field_value:
        slug = slugify(field_name)
        if not self.instance:
            l = set(self.Meta.model.objects.values_list("slug", flat=True))
        else:
            l = set(self.Meta.model.objects.exclude(id=self.instance.id).values_list("slug", flat=True))
        if slug in l:
            raise serializers.ValidationError(f"{field_name} must be unique")
        
