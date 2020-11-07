# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import FactureModel


# create a ModelForm
class FactureForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = FactureModel
        fields = "__all__"
