from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import EquipmentPartHistory
from django.contrib.contenttypes.models import ContentType
from project.models import Project


@receiver(post_save, sender=Project)
def create_ttd_history(sender, instance, created, **kwargs):
    if created:
        if instance.ttd:            
            for ttd in instance.ttd.all():
                obj = EquipmentPartHistory()
                
                EquipmentPartHistory.objects.create(
                    action_flag=1,
                    object_id=ttd.id,
                    content_type=ContentType.objects.get_for_model(ttd),
                )
