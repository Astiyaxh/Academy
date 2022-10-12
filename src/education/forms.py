from django import forms
from education import models

class EnglishInstituteRegisterForm(forms.ModelForm):
    class Meta:
        model = models.EnglishInstituteRegister
        fields = "__all__"
        exclude = ("user","institue_english","city","district","area","status","send_status","type")