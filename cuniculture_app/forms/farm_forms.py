from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, HiddenInput

from cuniculture_app.models.farms import Farm

class FarmForm(ModelForm):
    
    class Meta:
        model = Farm
        fields = ("farm_name","location", "in_charge", "in_charge_contact")

    def __init__(self, *args, **kwargs):
        super(FarmForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
