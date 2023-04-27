

from itertools import chain
from django import forms

from equipment.models import BDD, CALIBRATION_STAND, TTD
from .models import Project
from dal import autocomplete
from django.db.models import Q
# class ProjectForm(forms.ModelForm):

#     reactor = forms.ModelMultipleChoiceField(
#         queryset=Reactor.objects.all(),
#         widget = ModelSelect2MultipleWidget(
#             model = Reactor,
#             queryset=Reactor.objects.all(),
#             search_fields=['reactor_name__icontains'],
#             dependent_fields = {'unit':'unit'},
#             attrs={'data-placeholder': 'Search for reactor', 'data-width': '210px'},




#         )
#         )


        #     model=Reactor,
        #     queryset=Reactor.objects.all(),
        #     search_fields=['reactor_name__icontains'],
        #     dependent_fields = {'unit':'unit'},
        #     attrs={'data-placeholder': 'Search for Reactor', 'data-width': '250px'},






class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        if self.instance.id and self.instance.ttd:
            ids = []

            for i in TTD.objects.filter(ttd__ttd__isnull=True):
                ids.append(i.id)

            for i in self.instance.ttd.all():
                ids.append(i.id)
            print(len(ids))
            self.fields["ttd"].queryset = TTD.objects.filter(id__in=ids)
        else:
            
            self.fields["ttd"].queryset = TTD.objects.filter(
                ttd__ttd__isnull=True,)

        if self.instance.id and self.instance.bdd:
            ids = []
            
            for i in BDD.objects.filter(bdd__bdd__isnull=True):
                ids.append(i.id)
                
            for i in self.instance.bdd.all():
                ids.append(i.id)
                
            self.fields["bdd"].queryset = BDD.objects.filter(id__in =ids)

        else:
            queryset_1 = BDD.objects.filter(bdd__bdd__isnull=True)
            self.fields["bdd"].queryset = queryset_1

        if self.instance.id and self.instance.calibration_stand:
            ids = []
            for i in  CALIBRATION_STAND.objects.filter(
                calibration_stand__calibration_stand__isnull=True
            ):
                ids.append(i.id)

            for i in self.instance.calibration_stand.all():
                ids.append(i.id)

            self.fields["calibration_stand"].queryset = CALIBRATION_STAND.objects.filter(id__in = ids)

        else:
            queryset_1 = CALIBRATION_STAND.objects.filter(
                calibration_stand__calibration_stand__isnull=True
            )
            self.fields["calibration_stand"].queryset = queryset_1

    def clean(self):
        cleaned_data = self.cleaned_data

        if cleaned_data["project_end"] <= cleaned_data["project_start"]:
            raise forms.ValidationError(
                "Project end date can not be before the Project start date."
            )

        else:
            return cleaned_data
    # unit = forms.ModelChoiceField(queryset = Unit.objects.all(),required=False)
    # reactor = None
    class Meta:
        model = Project
        fields = ('__all__')
        widgets = {
            
            'reactor': autocomplete.ModelSelect2Multiple(url='reactor-autocomplete', forward=['client','unit'],attrs={'data-placeholder': 'Select Reactor'}),
            'unit': autocomplete.ModelSelect2(url='unit-autocomplete', forward=['client'], attrs={'data=placeholder': 'Select unit'}),
            # "project_start":DatePickerInput(options={"format": "DD/MM/YYYY"}),
            # "project_end":DatePickerInput(options={"format": "DD/MM/YYYY"}, range_from='project_start'),


        }
        
    