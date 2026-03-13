from django.db import models
from medical_profile.models import MedicalProfile

class QRCode(models.Model):
    profile = models.OneToOneField(MedicalProfile,on_delete=models.CASCADE)
    qr_image = models.ImageField(upload_to="qr_codes/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.profile.full_name)


