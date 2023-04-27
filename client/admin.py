from django.contrib import admin

from client.models import Address
from client.models import Client
from client.models import Reactor
from client.models import Plant

# from client.models import Contact
from client.models import Unit

# from client.forms import UnitModelForm

# from .forms import ReactorForm, UnitForm


class UnitAdmin(admin.ModelAdmin):
    # form = UnitForm
    # inlines = [
    #     LocaleTypeInline,
    # ]
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
    # def label_from_instance(self, obj):
    #      return "Plant: {}".format(obj.plant)

    class Media:
        # this path may be any you want,
        # just put it in your static folder
        js = ("js/admin/placeholder.js",)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.client == "plant":
    #         kwargs["queryset"] = Plant.objects.filter(plant__in=['God', 'Demi God'])
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
    # list_filter = (('client', admin.ChoiceDropdownFilter),)
    # list_filter = (('client', admin.DropdownFilter),)

    # def list_of_plant(self, obj):
    #     return ("%s" % ','.join([plant.plant_location for plant in obj.plant.all()]))
    # list_of_reactors.short_description = 'Reactors'
    # def has_module_permission(self, request):
    #     return False


admin.site.register(Unit, UnitAdmin)


class ReactorAdmin(admin.ModelAdmin):
    # form = ReactorForm
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
    }

    search_fields = ["reactor_name"]
    # def has_module_permission(self, request):
    #     return False


admin.site.register(Reactor, ReactorAdmin)


class PlantAdmin(admin.ModelAdmin):
    list_filter = ["client", "plant_location"]
    list_display = ("client", "plant_location", "plant_contact")

    # def list_of_units(self, obj):
    #     return ("%s" % ','.join([name_of_unit.name_of_unit for name_of_unit in obj.name_of_unit.all()]))
    # list_of_units.short_description = 'Units'
    # form = SimpleForm

    search_fields = ["plant_location", "client__official_name"]
    # def has_module_permission(self, request):
    #     return False


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


#     def has_module_permission(self, request):
#         return False

# admin.site.register(Contact,ContactAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ("City", "State", "Country", "Zipcode")
    search_fields = ["City"]

    def has_module_permission(self, request):
        return False


admin.site.register(Address, AddressAdmin)


from import_export.admin import ImportExportModelAdmin


class ClientAdmin(ImportExportModelAdmin):
    list_filter = ["official_name", "contact_person"]
    list_per_page = 5
    list_display = [
        "official_name",
        "contact_person",
        "contact_person_phone",
        "contact_person_email",
        "Official_Address",
        "Shipping_Address",
        "Plantentrance_address",
        "country",
    ]
    fieldsets = [
        (
            "Client Info",
            {
                "fields": [
                    "official_name",
                    "comman_name",
                    "alternate_name",
                    "parent_company",
                    "former_name",
                ],
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
    ]

    search_fields = ["official_name", "contact_person"]
    # list_filter=['contact_person']


admin.site.register(Client, ClientAdmin)
