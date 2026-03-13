from django.shortcuts import render,get_object_or_404
from lifesaverqr.medical_profile.models import MedicalProfile
from scan_tracking.models import ScanLog
from scan_tracking.utils import get_client_ip

def emergency_profile(request,uuid):
    profile = get_object_or_404(MedicalProfile,uuid = uuid)
    ip = get_client_ip(request)
    ScanLog.objects.create(
        profile=profile,
        ip_address=ip 
    )
    return render(request,"emergency/profile.html",{"profile":profile})
# Create your views here.
