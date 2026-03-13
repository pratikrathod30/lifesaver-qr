from django.db import models
from django.conf import settings
import uuid
# Create your models here.
class MedicalProfile(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    uuid =  models.UUIDField(default=uuid.uuid4,editable=False,unique=True)

    full_name = models.CharField(max_length=50)

    blood_group = models.CharField(max_length=3,choices=BLOOD_GROUP_CHOICES)

    allergies = models.TextField(blank=True)

    diseases = models.TextField(blank=True)

    emergency_contact = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.full_name

class MedicalReport(models.Model):
    profile = models.ForeignKey(MedicalProfile,on_delete=models.CASCADE,related_name="reports")
    report_file = models.FileField(upload_to="medical_reports/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.full_name} Report"