from ast import Return
from django.shortcuts import render,redirect,get_object_or_404
from .models import MedicalProfile,MedicalReport
from .forms import MedicalProfileForm,MedicalReportForm
from django.contrib.auth.decorators import login_required
from qr_system.services import generate_qr
from django.http import HttpResponseForbidden

@login_required
def create_profile(request):
    if request.method == "POST":
        form = MedicalProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            generate_qr(profile)
            return redirect("dashboard")
    else:
        form = MedicalProfileForm()
    return render(request,"profile/create_profile.html",{"form":form})

@login_required
def edit_profile(request):
    profile = get_object_or_404(MedicalProfile,user = request.user)
    if request.method == 'POST':
        form = MedicalProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = MedicalProfileForm(instance=profile)
    return render(request,"profile/edit_profile.html",{"form":form})

@login_required
def upload_report(request):
    profile = MedicalProfile.objects.get(user=request.user)

    if request.method == "POST":
        form = MedicalReportForm(request.POST,request.FILES)

        if form.is_valid():
            report = form.save(commit=False)
            report.profile = profile
            report.save()
            return redirect("dashboard")
    else:
        form = MedicalReportForm()
    return render(request,"profile/upload_report.html",{
        "form":form
        })

@login_required
def delete_report(request,report_id):
    report = get_object_or_404(MedicalReport,id=report_id,profile__user=request.user)
    report.delete()
    return redirect("dashboard")

@login_required
def doctor_view_profile(request,uuid):
    if request.user.role != "DOCTOR":
        return HttpResponseForbidden("Access Denied")
    profile = get_object_or_404(MedicalProfile , uuid=uuid)

    return render(request,"profile/doctor_view.html",{
        "profile":profile
    })
