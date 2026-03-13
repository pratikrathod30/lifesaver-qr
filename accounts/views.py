from django.shortcuts import render,redirect
from django.contrib.auth import logout , login , authenticate
from .forms import RegisterForm
from medical_profile.models import MedicalProfile
from django.contrib.auth.decorators import login_required
from scan_tracking.models import ScanLog
from django.http import HttpResponseForbidden
from qr_system.models import QRCode

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('login')
        return render(request, "accounts/register.html", {"form": form})
    else:
        form = RegisterForm()
        return render(request,"accounts/register.html",{"form":form})
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request , username = username , password = password)
        if user:
            login(request,user)
            return redirect("dashboard")
        return render(request,"accounts/login.html")
    return render(request,"accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("/accounts/login")

@login_required
def dashboard(request):
    role = request.user.role
    profile = MedicalProfile.objects.filter(user= request.user).first()
    scans = None
    reports = None
    qr=None
    total_scans = 0
    last_scan = None
    if profile:
        try:
            qr = QRCode.objects.get(profile=profile)
        except:
            qr = None
        scans = ScanLog.objects.filter(profile=profile).order_by("-timestamp")
        reports = profile.reports.all()
        total_scans=scans.count()
        last_scan = scans.first()

    return render(request , "dashboard/dashboard.html",{
        "profile":profile,
        "scans":scans,
        "reports":reports,
        "total_scans":total_scans,
        "last_scan":last_scan,
        "role":role,
        "qr":qr,
        })

@login_required
def admin_panel(request):
    if request.user.role  != "ADMIN":
        return HttpResponseForbidden("Access Denied")
    profiles = MedicalProfile.objects.all()
    scans = ScanLog.objects.all().order_by("-timestamp")

    return render(request,"admin/panel.html",{
        "profiles":profiles,
        "scans":scans
    })
def home(request):
    return render(request,"home.html")