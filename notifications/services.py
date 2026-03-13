from django.core.mail import send_mail
from django.conf import settings

def send_emergency_email(profile):
    subject = "Emergency Alert"
    message = f"Emergency QR Scanned for {profile.full_name}.Please check immediately"
    recipient_list = [profile.user.email]
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        recipient_list,
        fail_silently=False
    )