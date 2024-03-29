from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from client.models import Address, Client, Plant, Reactor, Unit

from .forms import ReactorForm, UnitForm


class UnitAdmin(admin.ModelAdmin):
    form = UnitForm

    list_filter = ["client", "plant"]
    list_display = (
        "client",
        "plant",
        "name_of_unit",
        "chemical_being_manufactured_by_this_unit",
    )
    list_filter = (
        "client",
        "plant",
        "name_of_unit",
    )

    search_fields = ["name_of_unit"]

    class Media:
        # this path may be any you want,
        # just put it in your static folder
        js = ("js/admin/placeholder.js",)


admin.site.register(Unit, UnitAdmin)


class ReactorAdmin(admin.ModelAdmin):
    form = ReactorForm

    def ttd_id(self, obj):
        if obj.tube_id and obj.input_tubeid:
            return f"{obj.input_tubeid} {obj.tube_id}"
        else:
            return "Not Available"

    ttd_id.short_description = "TTD ID "
    list_filter = ["client", "plant", "unit", "reactor_name"]
    list_display = (
        "client",
        "plant",
        "unit",
        "reactor_name",
        "ttd_id",
        "tube_material_of_tubes",
    )

    fieldsets = (
        (
            "Reactor Info",
            {
                "fields": (
                    "client",
                    "plant",
                    "unit",
                    "reactor_name",
                ),
            },
        ),
        (
            "Tube Info",
            {
                "fields": (
                    "tube_id",
                    "input_tubeid",
                    "is_there_ferrule_insert_in_tube",
                    "ferrule_length",
                    "input_ferrulelength",
                    "ferrule_id",
                    "input_ferruleid",
                    "tube_seal_type",
                ),
            },
        ),
        (
            "Number Of",
            {
                "fields": (
                    "tube_material_of_tubes",
                    "tube_material_of_raws",
                    "tube_material_of_thermo",
                    "thermo_couple_test",
                    "tube_material_of_supports",
                    "tube_material_of_plugs",
                    "tube_material_of_coolent_tubes",
                ),
            },
        ),
        (
            "Tube Specification",
            {
                "fields": (
                    "tube_spacing_or_pitch",
                    "input_tubespacing",
                    "total_tube_length",
                    "input_totaltube",
                    "top_tube_sheet_thickness",
                    "input_toptube",
                    "bottom_tube_sheet_thickness",
                    "input_bottomtube",
                ),
            },
        ),
        (
            "Tube Protude",
            {
                "fields": (
                    "tube_protude_out_of_top_tube_sheet",
                    "select_tube_protude_top",
                    "input_tubeprotude_top",
                    "tube_protude_out_of_bottom_tube_sheet",
                    "select_tube_protude_bottom",
                    "input_tubeprotude_bottom",
                    "top_dome_removable",
                    "top_inlet_accessible",
                    "top_inlet_impingment_plate",
                    "any_projections_on_tube_sheet_describe",
                    "tube_sheet_material",
                    "dom_material",
                ),
            },
        ),
        (
            "Tube Documents",
            {
                "fields": (
                    "tube_spacing_proof_document",
                    "reactor_tube_sheet_drawings",
                    "reactor_elevation_view_drawings",
                    "other_drawings",
                ),
            },
        ),
        (
            "Catalyst",
            {
                "fields": (
                    "catalyst_name",
                    "model_number",
                    # "reactor_elevation_view_drawings",
                    "manufacturer",
                    "shape",
                    "length",
                    "width",
                    "height",
                    "inner_diameter",
                    "outer_diameter",
                    "crush_strength",
                    "MSDS",
                ),
            },
        ),
        (
            "Loading",
            {
                "fields": (
                    "catalyst_to_be_loaded",
                    "layers_of_catalyst",
                    "layers_of_inerts",
                    "tube_loading_profile_drawing",
                    "loaded_tube_length_in",
                    "loaded_tube_length_mm",
                    "tube_bottom_retainer",
                    "top_spring",
                    "spring_height",
                    "spring_drawing",
                ),
            },
        ),
        (
            "Testing Speicification",
            {
                "fields": (
                    "supply_orifice_size",
                    "cal_orifice_size",
                    "pressure_sensor",
                    "expected_pressure_drop",
                    "calibrate_TTD_to",
                    "supply_pressure",
                ),
            },
        ),
    )

    radio_fields = {
        "tube_id": admin.HORIZONTAL,
        "is_there_ferrule_insert_in_tube": admin.HORIZONTAL,
        "ferrule_length": admin.HORIZONTAL,
        "ferrule_id": admin.HORIZONTAL,
        "tube_spacing_or_pitch": admin.HORIZONTAL,
        "total_tube_length": admin.HORIZONTAL,
        "top_tube_sheet_thickness": admin.HORIZONTAL,
        "bottom_tube_sheet_thickness": admin.HORIZONTAL,
        "tube_protude_out_of_top_tube_sheet": admin.HORIZONTAL,
        "tube_protude_out_of_bottom_tube_sheet": admin.HORIZONTAL,
        "top_dome_removable": admin.HORIZONTAL,
        "top_inlet_accessible": admin.HORIZONTAL,
        "top_inlet_impingment_plate": admin.HORIZONTAL,
        "select_tube_protude_top": admin.HORIZONTAL,
        "select_tube_protude_bottom": admin.HORIZONTAL,
        "thermo_couple_test": admin.HORIZONTAL,
    }

    search_fields = ["reactor_name"]


admin.site.register(Reactor, ReactorAdmin)


class PlantAdmin(admin.ModelAdmin):
    list_display = ("client", "plant_name", "plant_common_name")

    fieldsets = (
        (
            "Plant Info",
            {
                "fields": (
                    "client",
                    "plant_name",
                    "plant_common_name",
                ),
            },
        ),
        (
            "Address Info",
            {
                "fields": [
                    "official_address",
                    "shipping_address",
                    "plantentrance_address",
                    "country",
                ],
            },
        ),
        (
            "Contact Info",
            {
                "fields": [
                    "contact_person",
                    "contact_person_phone",
                    "contact_person_email",
                ],
            },
        ),
    )


admin.site.register(Plant, PlantAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "title",
        "company",
        "phone_office",
        "email",
    )
    search_fields = ["first_name"]

    class Media:
        # this path may be any you want,
        # just put it in your static folder
        js = ("js/admin/placeholder.js",)


class AddressAdmin(admin.ModelAdmin):
    list_display = ("City", "State", "Country", "Zipcode")
    search_fields = ["City"]

    def has_module_permission(self, request):
        return False


admin.site.register(Address, AddressAdmin)


class ClientAdmin(ImportExportModelAdmin):
    list_filter = ["official_name", "parent_company"]
    fieldsets = [
        (
            "Client Info",
            {
                "fields": [
                    "official_name",
                    "comman_name",
                    "parent_company",
                    "former_name",
                ],
            },
        ),
    ]

    search_fields = ["official_name", "contact_person"]


admin.site.register(Client, ClientAdmin)
