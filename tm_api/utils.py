from django.db.models import Q, F
from project.models import Project
from django.db.models.query import QuerySet

def filter_equipment_by_criteria(model_class, date_obj, p_qs, query, flags) -> QuerySet:
    qs = model_class.objects.filter(query)

    if date_obj:
        ids = get_ids(p_qs, **flags)
        qs = qs.exclude(id__in=ids)

    return qs

def get_ids(p_qs, **flags) -> set:
    ids = set()

    if flags.get("ttds") == 1:
        ids.update(p_qs.values_list("ttd", flat=True))
    if flags.get("bdds") == 1:
        ids.update(p_qs.values_list("bdd", flat=True))
    if flags.get("calis") == 1:
        ids.update(p_qs.values_list("calibration_stand", flat=True))
    if flags.get("swabs") == 1:
        ids.update(p_qs.values_list("swabmaster_equip", flat=True))
    
    return ids