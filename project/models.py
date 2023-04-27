from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from client.models import Client
from client.models import Unit
from equipment.models import TTD,BDD,CALIBRATION_STAND
import datetime
from part.models import Part
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail      
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from comment.models import Comment                                            
from django.contrib.auth.models import User

from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField
# import requests

# from notifications.signals import notify



class Scope_of_work(models.Model):
    name=models.CharField(max_length=128,default="")
    
    def __str__(self):
       return self.name


class ProjectStatus(models.Model):
    status = models.CharField(verbose_name = "Project Status", max_length =128 )
      
    def __str__(self):
        return self.status


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(null=True, blank=True, max_length =128, verbose_name = "Project Name")
    client=models.ForeignKey("client.Client",verbose_name="Client Name",default="",on_delete=models.CASCADE,null=True, blank=True)
    # chemical=models.OneToOneField("client.Unit",verbose_name="Chemical Name",default="",on_delete=models.CASCADE,blank=True,null=True,related_name="Chemical Name+") 
    unit=models.ForeignKey("client.Unit",verbose_name="Unit Name",default="",on_delete=models.CASCADE,null=True, blank=True, related_name = "unit")  
    reactor=models.ManyToManyField("client.Reactor",verbose_name="Reactor Name",null=True, blank=True)  
    # contact=models.ForeignKey(Contact,null=True,on_delete=models.SET_DEFAULT,default="",verbose_name="contact")
    project_number=models.IntegerField(default="1",blank=True,verbose_name="Project Number")
    project_status = models.ForeignKey(ProjectStatus,verbose_name="Project Status",on_delete=models.SET_NULL,null=True, blank=True)
    
    
    equipment_prep=models.DateField(("Equipment Prep"), default=datetime.date.today,blank=True)
    equipment_ready=models.DateField(("Equipment Ready"), default=datetime.date.today,blank=True)
    equipment_ship_client=models.DateField(("Equipment Ship Client"), default=datetime.date.today,blank=True)
    equipment_delivery_client=models.DateField(("Equipment Delivery Client"), default=datetime.date.today,blank=True)
    equipment_info_remarks=models.CharField(max_length=128,verbose_name="Equipment Info Remarks",default="",null=True, blank=True)
    project_start=models.DateField(("Project Start"), default=datetime.date.today,blank=True)
    project_end=models.DateField(("Project End"), default=datetime.date.today,blank=True)
    equipment_return_tubemaster=models.DateField(("Equipment Return Client"), default=datetime.date.today,blank=True)
    equipment_delivery_tubemaster=models.DateField(("Equipment Delivery Tubemaster"), default=datetime.date.today,blank=True)
    
    ttd=models.ManyToManyField("equipment.TTD",verbose_name="TTD",default="",null=True, blank=True, related_name='ttd')
    bdd=models.ManyToManyField("equipment.BDD",verbose_name="BDD",default="",null=True, blank=True,related_name='bdd')
    calibration_stand=models.ManyToManyField("equipment.CALIBRATION_STAND",verbose_name="CALIBRATION STAND",null=True, blank=True, related_name='calibration_stand')
    # ====================PARTS==================================
    part = models.ManyToManyField("part.Part", default="", null=True,blank=True)
    supply_orifice_part = models.ManyToManyField("part.Supply_orifice", default="", null=True,blank=True,verbose_name='Supply Orifice')
    pressure_sensor_part = models.ManyToManyField("part.Pressure_sensor", default="", null=True,blank=True,verbose_name="Pressure Sensor")
    # ttd_part = models.ManyToManyField("part.TTD_tube_seal_rack", default="", null=True,blank=True,verbose_name="TTD tube Seal Rack")
    # bdd_part = models.ManyToManyField("part.BDD_tube_seal_rack", default="", null=True,blank=True,verbose_name="BDD Tube Seal Rack")
    calibration_orifice_part = models.ManyToManyField("part.Calibration_orifice", default="", null=True,blank=True,verbose_name="Calibration Orifice")
    swabmaster_part = models.ManyToManyField("part.SwabMasterTSR", default="", null=True,blank=True,verbose_name="Swab Master TSR")
    device_part = models.ManyToManyField("part.DeviceHose", default="", null=True,blank=True,verbose_name="Device Hose")
    airhose_part = models.ManyToManyField("part.AirHose", default="", null=True,blank=True,verbose_name="Air Hose")
    
    comments = GenericRelation(Comment)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    # class scope_of_work(models.TextChoices):
    #   PD_TESTING='PD_TESTING',('PD_TESTING')
    #   BD='BD',('BD')
    #   TC='TC',('TC')
    #   JAC='JAC',('JAC')
    #   OLE='OLE',('OLE')
    #   FULL_TURN_KEY='FULL_TURN_KEY',('FULL_TURN_KEY')
    #   OTHER='OTHER',('OTHER')
    
    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.pk})
      
    scope_of_work=models.ManyToManyField(Scope_of_work,verbose_name="Scope Of Work")
    
    class contract(models.TextChoices):
      DIRECT='DIRECT',('DIRECT')
      SUB='SUB',('SUB')
    contract=models.CharField(max_length=128,verbose_name="Contract",choices= contract.choices,default="",null=True, blank=True)
    if_sub_client_name=models.CharField(max_length=128,blank=True,verbose_name="If Sub Contract Then Client Name")
    general_remarks=models.CharField(max_length=128,verbose_name="General Remarks",default="",null=True, blank=True)
 
    
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

# =======================================================

    def Supply_Orifice(self):
        if self.supply_orifice_part:
            return ",".join([str(i) for i in self.supply_orifice_part.all()])
        
        else:
            return "-"

    def Pressure_Sensor(self):
        if self.pressure_sensor_part:
            return ",".join([str(i) for i in self.pressure_sensor_part.all()])
        
        else:
            return "-"
            
    # def calibration_stands(self):
    #     if self.calibration_stand:
    #         return ",".join([str(i) for i in self.calibration_stand.all()])
        
    #     else:
    #         return "-"


    def calibration_orifice(self):
        if self.calibration_orifice_part:
            return ",".join([str(i) for i in self.calibration_orifice_part.all()])
        
        else:
            return "-"
            
    def swabmaster(self):
        if self.swabmaster_part:
            return ",".join([str(i) for i in self.swabmaster_part.all()])
        
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
            return ['-']
            

        
    def Last_Comment(self):
        qs = Comment.objects.filter(content_type=33, object_id = self.id)
        if qs.exists():
            
            return qs[0]
        else:
            return "-"

            
# @receiver(post_save, sender=Project)
# def Project_post_save_receiver(sender,instance,created, **kwargs):
#   if created:

#     send_mail(
#       'Confirmation Email',
#       "Here is the message",
#       settings.EMAIL_HOST_USER,
#       [instance.created_by.email],
#       fail_silently=True,
      
#     )
#     print("email sent successfully")
#   else:
#     return

# @receiver(post_save, sender=Project)

# def my_handler(sender, instance, created, **kwargs):
#     notify.send(sender,
#     recipient= instance.created_by,
#     verb= instance.client,
#     description = f"A new new project is created.",
#     # timestamp = timezone.now()
#     )

# post_save.connect(my_handler, sender=Project)