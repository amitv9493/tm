from django.db.models import Q, F
from project.models import Project

def filter_equipment_by_criteria(model_class, date_obj, slug, pm_status, search, flags):
    qs = model_class.objects.all()

    if slug:
        qs = qs.filter(location_for_warehouse__slug=slug)

    if pm_status != "NONE":
        qs = qs.filter(pm_status=pm_status)

    if search != "None":
        query = Q()
        query |= (
            Q(abbreviation__icontains=search)
            | Q(alternate_name__icontains=search)
            | Q(serial_number__icontains=search)
            | Q(asset_number__icontains=search)
            | Q(packaging__icontains=search)
        )
        qs = qs.filter(query)

    if date_obj:
        ids = get_ids(date_obj, **flags)
        qs = qs.exclude(id__in=ids)

    return qs

def get_ids(date_obj, **flags) -> set:
    ids = set()
    p_qs = Project.objects.annotate(
        ttd_count=F("ttd__id"),
        bdd_count=F("bdd__id"),
        cali_count=F("calibration_stand__id"),
        swab_count=F("swabmaster_equip__id"),
    ).filter(equipment_delivery_client__gt=date_obj)

    if flags.get("ttds") == 1:
        ids.update(p_qs.values_list("ttd_count", flat=True))
    if flags.get("bdds") == 1:
        ids.update(p_qs.values_list("bdd_count", flat=True))
    if flags.get("calis") == 1:
        ids.update(p_qs.values_list("cali_count", flat=True))
    if flags.get("swabs") == 1:
        ids.update(p_qs.values_list("swab_count", flat=True))

    return ids
