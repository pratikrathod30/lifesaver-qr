from django.contrib import admin
from .models import MedicalProfile,MedicalReport
# Register your models here.

admin.site.register(MedicalProfile)
admin.site.register(MedicalReport)