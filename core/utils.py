from django.db.models import Q
from project.models import Project

def get_exclude_objects(start_date, part_name) -> set:
    
    if start_date:
        exclude_objects = set(Project.objects.filter(
            equipment_delivery_tubemaster__gte=start_date,
        ).values_list(part_name, flat=True))

        return exclude_objects
    return []