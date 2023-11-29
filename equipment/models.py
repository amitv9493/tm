from django import forms
from django.db import models
from django.utils.text import slugify

from project.validators import slugFieldValidator


class TTD(models.Model):
    abbreviation = models.CharField(max_length=128, blank=True, null=True)
    alternate_name = models.CharField(
        max_length=128, verbose_name="Alternate Name", blank=True, null=True
    )
    serial_number = models.CharField(
        max_length=128,
        verbose_name="Serial Number",
    )
    asset_number = models.CharField(
        max_length=128, null=True, blank=True, verbose_name="Asset Number"
    )

    class pm_status(models.TextChoices):
        RED = "RED", ("RED")
        BLUE = "BLUE", ("BLUE")
        GREEN = "GREEN", ("GREEN")

    pm_status = models.CharField(
        max_length=20,
        choices=pm_status.choices,
        verbose_name="PM Status",
        null=True,
        blank=True,
    )
    remarks = models.CharField(blank=True, null=True, max_length=999)

    location_for_warehouse = models.ForeignKey(
        "tube.Warehouse",
        verbose_name="Location For Warehouse",
        null=True,
        on_delete=models.SET_NULL,
        related_name="ttd",
    )
    location_for_storage = models.CharField(
        max_length=128, blank=True, verbose_name="Location For Storage"
    )
    packaging = models.CharField(max_length=128, blank=True)

    class is_this_part_of_set(models.TextChoices):
        YES = "YES", ("YES")
        NO = "NO", ("NO")

    is_this_part_of_set = models.CharField(
        max_length=128,
        choices=is_this_part_of_set.choices,
        verbose_name="Is This Part Of Set",
        null=True,
        blank=True,
    )
    if_yes_how_many_in_a_set = models.CharField(
        max_length=128, blank=True, verbose_name="If Yes How Many In A Set?"
    )

    supply_orifice_set = models.OneToOneField(
        "part.Supply_orifice",
        verbose_name="Supply Orifice Set",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="TTD",
    )
    pressure_sensor = models.OneToOneField(
        "part.Pressure_sensor",
        verbose_name="Pressure Sensor",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="TTD",
    )
    TTD_tube_seal_rack = models.OneToOneField(
        "part.TTD_tube_seal_rack",
        verbose_name="TTD Tube Seal Rack",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="TTD",
    )
    frame = models.CharField(max_length=128, blank=True)
    image = models.ImageField(upload_to="uploads/ttd/", blank=True)
    slug = models.SlugField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "TTD"

    class ttdChoiceField(forms.ModelChoiceField):
        def label_from_instance(self, obj):
            return f"{obj.serial_number} - {obj.pm_status}"

    def __str__(self):
        return (
            f"{self.serial_number} - {self.pm_status} - {self.location_for_warehouse}"
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.serial_number)
        return super(TTD, self).save(*args, **kwargs)

    def clean_serial_number(self):
        value = self.serial_number
        try:
            id = self.id
        except Exception:
            id = None

        qs = TTD.objects.all()
        slugFieldValidator(value, qs, "Serial Number", id)

    def clean(self):
        super().clean()  # Call the parent's clean() method

        self.clean_serial_number()


class BDD(models.Model):
    abbreviation = models.CharField(max_length=128, blank=True)
    alternate_name = models.CharField(
        max_length=128, blank=True, verbose_name="Alternate Name"
    )
    serial_number = models.CharField(max_length=128, verbose_name="Serial Number")
    asset_number = models.CharField(
        max_length=128, blank=True, verbose_name="Asset Number"
    )

    class pm_status(models.TextChoices):
        RED = "RED", ("RED")
        BLUE = "BLUE", ("BLUE")
        GREEN = "GREEN", ("GREEN")

    pm_status = models.CharField(
        max_length=20,
        choices=pm_status.choices,
        verbose_name="PM Status",
        null=True,
        blank=True,
    )
    remarks = models.CharField(blank=True, null=True, max_length=999)

    location_for_warehouse = models.ForeignKey(
        "tube.Warehouse",
        verbose_name="Location For Warehouse",
        on_delete=models.SET_NULL,
        null=True,
        related_name="bdd",
    )
    location_for_storage = models.CharField(
        max_length=128, blank=True, verbose_name="Location For Storage"
    )
    packaging = models.CharField(max_length=128, blank=True)

    class is_this_part_of_set(models.TextChoices):
        YES = "YES", ("YES")
        NO = "NO", ("NO")

    is_this_part_of_set = models.CharField(
        max_length=128,
        choices=is_this_part_of_set.choices,
        verbose_name="Is This Part Of Set?",
        null=True,
        blank=True,
    )
    if_yes_how_many_in_a_set = models.CharField(
        max_length=128, blank=True, verbose_name="If Yes How Many In A Set?"
    )
    BDD_tube_seal_rack = models.OneToOneField(
        "part.BDD_tube_seal_rack",
        verbose_name="BDD Tube Seal Rack",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="bdd",
    )
    frame = models.CharField(max_length=128, blank=True)
    image = models.ImageField(upload_to="uploads/bdd/", default="", blank=True)
    slug = models.SlugField(max_length=500, null=True, blank=True)

    def __str__(self):
        return (
            f"{self.serial_number} - {self.pm_status} - {self.location_for_warehouse}"
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.serial_number)
        print(self.slug)
        return super(BDD, self).save(*args, **kwargs)

    def clean_serial_number(self):
        value = self.serial_number
        try:
            id = self.id
        except Exception:
            id = None

        qs = BDD.objects.all()
        slugFieldValidator(value, qs, "Serial Number", id)

    def clean(self):
        super().clean()  # Call the parent's clean() method

        self.clean_serial_number()

    class Meta:
        verbose_name = "BDD"

    class bddChoiceField(forms.ModelChoiceField):
        def label_from_instance(self, obj):
            return f" {obj.serial_number} - {obj.pm_status} "


class CALIBRATION_STAND(models.Model):
    abbreviation = models.CharField(max_length=128, blank=True)
    alternate_name = models.CharField(
        max_length=128, blank=True, verbose_name="Alternate Name"
    )
    serial_number = models.CharField(
        max_length=128, blank=True, verbose_name="Serial Number"
    )
    asset_number = models.CharField(
        max_length=128, blank=True, verbose_name="Asset Number"
    )

    class pm_status(models.TextChoices):
        RED = "RED", ("RED")
        BLUE = "BLUE", ("BLUE")
        GREEN = "GREEN", ("GREEN")

    pm_status = models.CharField(
        max_length=20,
        choices=pm_status.choices,
        verbose_name="PM Status",
        null=True,
        blank=True,
    )
    remarks = models.CharField(blank=True, null=True, max_length=999)

    location_for_warehouse = models.ForeignKey(
        "tube.Warehouse",
        verbose_name="Location For Warehouse",
        on_delete=models.SET_NULL,
        null=True,
        related_name="calibration_stand",
    )
    location_for_storage = models.CharField(
        max_length=128, blank=True, verbose_name="Location For Storage"
    )
    packaging = models.CharField(max_length=128, blank=True)

    class is_this_part_of_set(models.TextChoices):
        YES = "YES", ("YES")
        NO = "NO", ("NO")

    is_this_part_of_set = models.CharField(
        max_length=128,
        choices=is_this_part_of_set.choices,
        verbose_name="Is This Part Of Set?",
        default=is_this_part_of_set.YES,
        blank=True,
    )
    if_yes_how_many_in_a_set = models.CharField(
        max_length=128, blank=True, verbose_name="If Yes How Many In A Set?"
    )
    cal_stand_size = models.CharField(
        max_length=128, blank=True, verbose_name="Calibration Stand Size"
    )
    calibration_orifice_set = models.OneToOneField(
        "part.Calibration_orifice",
        verbose_name="Calibration Orifice Set",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="calibration",
    )
    frame = models.CharField(max_length=128, blank=True)
    image = models.ImageField(upload_to="uploads/cal_stand/", blank=True)
    slug = models.SlugField(max_length=500, null=True, blank=True)

    def __str__(self):
        return (
            f"{self.serial_number} - {self.pm_status} - {self.location_for_warehouse}"
        )

    class Meta:
        verbose_name = "Calibration Rack"

    class calibrationChoiceField(forms.ModelChoiceField):
        def label_from_instance(self, obj):
            return f" {obj.serial_number} - {obj.pm_status} "

    def save(self, *args, **kwargs):
        self.slug = slugify(self.serial_number)
        print(self.slug)
        return super(CALIBRATION_STAND, self).save(*args, **kwargs)

    def clean_serial_number(self):
        value = self.serial_number
        try:
            id = self.id
        except Exception:
            id = None

        qs = CALIBRATION_STAND.objects.all()
        slugFieldValidator(value, qs, "Serial Number", id)

    def clean(self):
        super().clean()  # Call the parent's clean() method

        self.clean_serial_number()


class SwabMaster(models.Model):

    """Warehouse Info"""

    location_for_warehouse = models.ForeignKey(
        "tube.Warehouse",
        verbose_name="Location For Warehouse",
        on_delete=models.SET_NULL,
        null=True,
        related_name="swabmaster",
    )
    location_for_storage = models.CharField(
        max_length=128, blank=True, null=True, verbose_name="Location For Storage"
    )
    packaging = models.CharField(max_length=128, blank=True, null=True)

    class is_this_part_of_set(models.TextChoices):
        YES = "YES", ("YES")
        NO = "NO", ("NO")

    is_this_part_of_set = models.CharField(
        max_length=128,
        choices=is_this_part_of_set.choices,
        verbose_name="Is This Part Of Set",
        null=True,
        blank=True,
    )
    if_yes_how_many_in_a_set = models.CharField(
        max_length=128, blank=True, verbose_name="If Yes How Many In A Set?"
    )

    abbreviation = models.CharField(max_length=128, blank=True, null=True)
    alternate_name = models.CharField(
        max_length=128, blank=True, null=True, verbose_name="Alternate Name"
    )
    serial_number = models.CharField(
        max_length=128, blank=True, null=True, verbose_name="Serial Number"
    )
    asset_number = models.CharField(
        max_length=128, blank=True, null=True, verbose_name="Asset Number"
    )

    class pm_status(models.TextChoices):
        RED = "RED", ("RED")
        BLUE = "BLUE", ("BLUE")
        GREEN = "GREEN", ("GREEN")

    pm_status = models.CharField(
        max_length=20,
        choices=pm_status.choices,
        verbose_name="PM Status",
        blank=True,
        null=True,
    )
    remarks = models.CharField(blank=True, null=True, max_length=999)

    """specification"""

    Swab_Master_Tube_Seal_Rack = models.OneToOneField(
        "part.SwabMasterTSR",
        blank=True,
        null=True,
        verbose_name=("SwabMaster Tube Seal Rack"),
        on_delete=models.SET_NULL,
        related_name="swabmaster",
    )
    Generation_1 = models.CharField(
        choices=is_this_part_of_set.choices, max_length=3, null=True, blank=True
    )
    Generation_2 = models.CharField(
        choices=is_this_part_of_set.choices, max_length=3, null=True, blank=True
    )
    slug = models.SlugField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.serial_number} {self.pm_status}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.serial_number)
        print(self.slug)
        return super(SwabMaster, self).save(*args, **kwargs)

    def clean_serial_number(self):
        value = self.serial_number
        try:
            id = self.id
        except Exception:
            id = None

        qs = SwabMaster.objects.all()
        slugFieldValidator(value, qs, "Serial Number", id)

    def clean(self):
        super().clean()  # Call the parent's clean() method

        self.clean_serial_number()

    class Meta:
        verbose_name = "Swab Master"
