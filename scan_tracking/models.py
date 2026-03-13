from django.db import models
from medical_profile.models import MedicalProfile

class ScanLog(models.Model):
    profile = models.ForeignKey(MedicalProfile,on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    location = models.CharField(max_length=255,blank=True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.profile.full_name)
# Create your models here.
