from django.db import models
import datetime
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from comment.models import Comment
from django.utils.text import slugify
from project.validators import slugFieldValidator


class Scope_of_work(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class ProjectStatus(models.Model):
    status = models.CharField(verbose_name="Project Status", max_length=128)

    def __str__(self):
        return self.status


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=128, verbose_name="Project Name", unique=True)
    slug = models.SlugField()
    client = models.ForeignKey(
        "client.Client",
        verbose_name="Client Name",
        default="",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    unit = models.ForeignKey(
        "client.Unit",
        verbose_name="Unit Name",
        default="",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="unit",
    )
    reactor = models.ManyToManyField(
        "client.Reactor", verbose_name="Reactor Name", blank=True
    )
    project_number = models.IntegerField(
        default="1", blank=True, verbose_name="Project Number"
    )
    project_status = models.ForeignKey(
        ProjectStatus,
        verbose_name="Project Status",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    equipment_prep = models.DateField(
        ("Equipment Prep"), default=datetime.date.today, blank=True
    )
    equipment_ready = models.DateField(
        ("Equipment Ready"), default=datetime.date.today, blank=True
    )
    equipment_ship_client = models.DateField(
        ("Equipment Ship Client"), default=datetime.date.today, blank=True
    )
    equipment_delivery_client = models.DateField(
        ("Equipment Delivery Client"), default=datetime.date.today, blank=True
    )
    equipment_info_remarks = models.CharField(
        max_length=128,
        verbose_name="Equipment Info Remarks",
        default="",
        null=True,
        blank=True,
    )
    project_start = models.DateField(
        ("Project Start"), default=datetime.date.today, blank=True
    )
    project_end = models.DateField(
        ("Project End"), default=datetime.date.today, blank=True
    )
    equipment_return_tubemaster = models.DateField(
        ("Equipment Return Client"), default=datetime.date.today, blank=True
    )
    equipment_delivery_tubemaster = models.DateField(
        ("Equipment Delivery Tubemaster"), default=datetime.date.today, blank=True
    )
    # ==================== EQUIPMENT ==================================

    ttd = models.ManyToManyField(
        "equipment.TTD", verbose_name="TTD", default="", blank=True, related_name="ttd"
    )
    bdd = models.ManyToManyField(
        "equipment.BDD", verbose_name="BDD", default="", blank=True, related_name="bdd"
    )
    calibration_stand = models.ManyToManyField(
        "equipment.CALIBRATION_STAND",
        verbose_name="CALIBRATION STAND",
        blank=True,
        related_name="calibration_stand",
    )

    swabmaster_equip = models.ManyToManyField(
        "equipment.SwabMaster",
        verbose_name=("Swab Master"),
        related_name="Swabmaster",
        blank=True,
    )

    # ====================PARTS==================================
    part = models.ManyToManyField(
        "part.Part", default="", blank=True, related_name="projects"
    )

    calibration_orifice_part = models.ManyToManyField(
        "part.Calibration_orifice",
        default="",
        blank=True,
        verbose_name="Calibration Orifice",
        related_name="projects",
    )

    device_part = models.ManyToManyField(
        "part.DeviceHose",
        default="",
        blank=True,
        verbose_name="Device Hose",
        related_name="projects",
    )
    airhose_part = models.ManyToManyField(
        "part.AirHose",
        default="",
        blank=True,
        verbose_name="Air Hose",
        related_name="projects",
    )

    comments = GenericRelation(Comment)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.pk})

    scope_of_work = models.ManyToManyField(
        Scope_of_work, verbose_name="Scope Of Work", blank=True
    )

    class contract(models.TextChoices):
        DIRECT = "DIRECT", ("DIRECT")
        SUB = "SUB", ("SUB")

    contract = models.CharField(
        max_length=128,
        verbose_name="Contract",
        choices=contract.choices,
        default="",
        null=True,
        blank=True,
    )
    if_sub_client_name = models.CharField(
        max_length=128, blank=True, verbose_name="If Sub Contract Then Client Name"
    )
    general_remarks = models.CharField(
        max_length=128,
        verbose_name="General Remarks",
        default="",
        null=True,
        blank=True,
    )

    def Reactor(self):
        if self.reactor:
            return ",".join([str(i) for i in self.reactor.all()])
        else:
            return "-"

    def work_scope(self):
        if self.scope_of_work:
            return ",".join([str(i) for i in self.scope_of_work.all()])
        else:
            return "-"

    def ttds(self):
        if self.ttd:
            return ",".join([str(i) for i in self.ttd.all()])
        else:
            return "-"

    def bdds(self):
        if self.bdd:
            return ",".join([str(i) for i in self.bdd.all()])

        else:
            return "-"

    def calibration_stands(self):
        if self.calibration_stand:
            return ",".join([str(i) for i in self.calibration_stand.all()])

        else:
            return "-"

    def calibration_orifice(self):
        if self.calibration_orifice_part:
            return ",".join([str(i) for i in self.calibration_orifice_part.all()])

        else:
            return "-"

    def device_Hose(self):
        if self.device_part:
            return ",".join([str(i) for i in self.device_part.all()])

        else:
            return "-"

    def Air_Hose(self):
        if self.airhose_part:
            return ",".join([str(i) for i in self.airhose_part.all()])

        else:
            return ["-"]

    def Last_Comment(self):
        qs = Comment.objects.filter(content_type=33, object_id=self.id)
        if qs.exists():
            return qs[0]
        else:
            return "-"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.project_name)
        return super(Project, self).save(*args, **kwargs)

    def clean_project_name(self):
        value = self.project_name
        try:
            id = self.id
        except:
            id = None

        qs = Project.objects.all()
        slugFieldValidator(value, qs, "Project Name", id)

    def clean(self):
        super().clean()  # Call the parent's clean() method

        self.clean_project_name()
