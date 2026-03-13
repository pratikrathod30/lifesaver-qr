from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from medical_profile.models import MedicalProfile,MedicalReport
from .serializers import MedicalProfileSerializer,MedicalReportSerializer,UserRegisterSerializer
from django.shortcuts import get_object_or_404
from scan_tracking.models import ScanLog
from .serializers import ScanLogSerializer
from accounts.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse

@api_view(["GET"])
def profile_api(request,uuid):
    profile = get_object_or_404(MedicalProfile,uuid=uuid)
    serializer = MedicalProfileSerializer(profile)
    return Response(serializer.data)

@api_view(["GET"])
def reports_api(request,uuid):
    profile = get_object_or_404(MedicalProfile,uuid = uuid)
    reports = MedicalReport.objects.filter(profile=profile)
    serializer = MedicalReportSerializer(reports,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def scans_api(request,uuid):
    profile = get_object_or_404(MedicalProfile,uuid = uuid)
    scans = ScanLog.objects.filter(profile = profile)

    serializer = ScanLogSerializer(scans,many=True)

    return Response(serializer.data)

@api_view(["POST"])
def register_api(request):
    serializer = UserRegisterSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["POST"])
def login_api(request):

    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user:
        return Response({
            "message": "Login successful",
            "username": user.username,
            "role": user.role
        })

    return Response({
        "error": "Invalid credentials"
    })
from django.http import JsonResponse
from scan_tracking.models import ScanLog

def save_location(request):

    lat = request.GET.get("lat")
    lon = request.GET.get("lon")
    uuid = request.GET.get("uuid")

    try:
        profile = MedicalProfile.objects.get(uuid=uuid)
        scan = ScanLog.objects.filter(profile=profile).last()

        if scan:
            scan.location = f"{lat},{lon}"
            scan.save()

    except:
        pass

    return JsonResponse({"status":"ok"})