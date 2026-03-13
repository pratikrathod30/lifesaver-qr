from django.shortcuts import render,get_object_or_404
from medical_profile.models import MedicalProfile
from notifications.services import send_emergency_email
from scan_tracking.models import ScanLog
from scan_tracking.utils import get_client_ip
from medical_profile.models import MedicalProfile
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from .models import QRCode

import requests

def emergency_profile(request, uuid):

    profile = get_object_or_404(MedicalProfile, uuid=uuid)

 
    ip = get_client_ip(request)

    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=3)
        ip_data = response.json()
        city = ip_data.get("city")
        country = ip_data.get("country")
        location = f"{city}, {country}"
    except:
        location = "Unknown"

    hospital_list = []

    try:
        lat = request.GET.get("lat")
        lon = request.GET.get("lon")

        if lat and lon:

            query = f"""
            [out:json];
            (
              node["amenity"="hospital"](around:3000,{lat},{lon});
            );
            out body;
            """

            url = "https://overpass-api.de/api/interpreter"

            res = requests.get(url, params={'data': query}, timeout=5)
            hospital_data = res.json()

            hospitals = []

            for item in hospital_data.get("elements", []):
                name = item.get("tags", {}).get("name")

                if name:
                    dist = (
                        (float(item["lat"]) - float(lat)) ** 2 +
                        (float(item["lon"]) - float(lon)) ** 2
                    )

                    hospitals.append((name, dist))

          
            hospitals.sort(key=lambda x: x[1])

           
            hospital_list = [h[0] for h in hospitals[:5]]

    except:
        hospital_list = []
    ScanLog.objects.create(
        profile=profile,
        ip_address=ip,
        location=location
    )

    return render(request, "emergency/profile.html", {
        "profile": profile,
        "hospitals": hospital_list
    })


@login_required
def download_qr(request):
    qr = QRCode.objects.get(profile__user = request.user)
    return FileResponse(qr.qr_image.open(),as_attachment=True)

