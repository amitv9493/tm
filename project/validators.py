from django.utils.text import slugify
from django.core.exceptions import ValidationError


# Create your models here.
def slugFieldValidator(value, qs, id=None):
    if id:
        if slugify(value) in qs.exclude(id=id).values_list("slug", flat=True):
            raise ValidationError("please input a unique name")
    return value
