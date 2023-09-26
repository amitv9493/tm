from django.core.management.base import BaseCommand
from project.models import Project
from datetime import timedelta
from equipment.models import *
from part.models import *


class Command(BaseCommand):
    
    help = "If the project has expired and it has more than 24 hours, the parts will be set to RED"

    def handle(self, *args, **options):
        from django.utils import timezone
        now = timezone.now()
        projects = Project.objects.filter(
            equipment_delivery_tubemaster__lte = now - timedelta(days=1)
        )

        if projects.exists():
            self.stdout.write(self.style.NOTICE(f"found {projects.count()} projects"))
            parts = set(projects.values_list("part", flat=True))
            ttds = set(projects.values_list("ttd", flat=True))
            bdds = set(projects.values_list("bdd", flat=True))
            calibration_stands = set(
                projects.values_list("calibration_stand", flat=True)
            )
            swabmaster_equip = set(
                projects.values_list("swabmaster_equip", flat=True)
            )
            calibration_orifice_part = set(
                projects.values_list("calibration_orifice_part", flat=True)
            )
            device_part = set(projects.values_list("device_part", flat=True))
            airhose_part = set(projects.values_list("airhose_part", flat=True))
            
            Part.objects.filter(id__in=parts).update(pm_status="RED")
            TTD.objects.filter(id__in=ttds).update(pm_status="RED")
            BDD.objects.filter(id__in=bdds).update(pm_status="RED")
            CALIBRATION_STAND.objects.filter(id__in=calibration_stands).update(
                pm_status="RED"
            )

            SwabMaster.objects.filter(id__in=swabmaster_equip).update(pm_status="RED")
            Calibration_orifice.objects.filter(id__in=calibration_orifice_part).update(
                pm_status="RED"
            )
            DeviceHose.objects.filter(id__in=device_part).update(pm_status="RED")
            AirHose.objects.filter(id__in=airhose_part).update(pm_status="RED")

            self.stdout.write(self.style.SUCCESS(f"Successfully ran job on : {now}"))

            self.stdout.write(self.style.SUCCESS(f"Updated ttds: {len(ttds)}"))
            self.stdout.write(self.style.SUCCESS(f"Updated bdds: {len(bdds)}"))
            self.stdout.write(self.style.SUCCESS(f"Updated calibration_stands: {len(calibration_stands)}"))
            self.stdout.write(self.style.SUCCESS(f"Updated swabmaster_equip: {len(swabmaster_equip)}"))
            self.stdout.write(self.style.SUCCESS(f"Updated calibration_orifice_part: {len(calibration_orifice_part)}"))
            self.stdout.write(self.style.SUCCESS(f"Updated device_part: {len(device_part)}"))
            self.stdout.write(self.style.SUCCESS(f"Updated airhose_part: {len(airhose_part)}"))
                    
        else:
            self.stdout.write(self.style.SUCCESS("Successfully ran the command No Projects Found"))
