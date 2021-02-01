from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, HiddenInput, DateInput
from crispy_forms.layout import Layout

from cuniculture_app.models.livestocks import Livestock, Deaths, Sales, SalesDetails

class LivestockForm(ModelForm):
    
    class Meta:
        model = Livestock
        fields = ("livestock_type","breed_category", "farm", "male", "female", "maturity", "maturity_period", "available_stock", "status")

    def __init__(self, *args, **kwargs):
        super(LivestockForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

class DeathsForm(ModelForm):
    
    class Meta:
        model = Deaths
        fields = ("death_date", "livestock", "farm", "gender", "quantity", "cause")

        widgets = {
            'death_date': DateInput(format=('%m/%d/%Y'), attrs={'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(DeathsForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

class SalesForm(ModelForm):
    
    class Meta:
        model = Sales
        fields = ("client",)

        widgets = {
            'sales_date': DateInput(format=('%m/%d/%Y'), attrs={'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(SalesForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

class SalesDetailsForm(ModelForm):
    
    class Meta:
        model = SalesDetails
        fields = ("sale", "livestock", "farm", "male", "female", "rate", "amount",)

    def __init__(self, *args, **kwargs):
        super(SalesDetailsForm, self).__init__(*args, **kwargs)

        self.fields["sale"].widget = HiddenInput()

        self.helper = FormHelper()
