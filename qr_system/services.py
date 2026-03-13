import qrcode
from io import BytesIO
from django.core.files import File
from .models import QRCode

def generate_qr(profile):
    if QRCode.objects.filter(profile=profile).exists():
        return QRCode.objects.get(profile=profile)
    url = f"https://recompensatory-unimplicitly-margret.ngrok-free.dev/emergency/{profile.uuid}/"
    qr = qrcode.make(url)
    buffer = BytesIO()
    qr.save(buffer)

    qr_code = QRCode(profile = profile)
    qr_code.qr_image.save(f"{profile.uuid}.png",File(buffer),save=True)

    return qr_code