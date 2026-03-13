from django import forms
from .models import MedicalProfile,MedicalReport

class MedicalProfileForm(forms.ModelForm):
    class Meta:
        model  = MedicalProfile
        fields = [
            "full_name",
            "blood_group",
            "allergies",
            "diseases",
            "emergency_contact",
        ]

class MedicalReportForm(forms.ModelForm):
    class Meta:
        model = MedicalReport
        fields = ["report_file"]