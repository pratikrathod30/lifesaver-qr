from django.urls import path
from .views import emergency_profile,download_qr

urlpatterns = [  
    path("download/",download_qr,name="download_qr"),
    path("<uuid:uuid>/",emergency_profile,name="emergency_profile"),
  
]