from django import forms
from education import models

class EnglishInstituteRegisterForm(forms.ModelForm):
    class Meta:
        model = models.EnglishInstituteRegister
        fields = "__all__"
        exclude = ("status","send_status","type")


class NonprofitInstituteRegisterForm(forms.ModelForm):
    class Meta:
        model = models.NonprofitInstituteRegister
        fields = "__all__"
        exclude = ("status","send_status","type")