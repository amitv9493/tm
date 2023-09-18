from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class ACTION_FLAGS(models.TextChoices):
    ADDED = 1
    DISMANTLED = 0
    
class ModelHistory(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    action_flag = models.CharField(max_length=1, choices=ACTION_FLAGS.choices)
    
    class Meta:
        abstract = True
        
class EquipmentPartHistory(ModelHistory):
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = "Equipment Part History"
        db_table = 'equipment_part_history'
    
    def __str__(self):
        return f'{self.content_object} {self.get_action_flag_display()} by {self.user}'