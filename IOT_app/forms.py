from django.forms import ModelForm
from .models import Bin1

class DataForm(ModelForm):
    class Meta:
        model=Bin1
        fields=['value',]
