from django.urls import path
from .views import create_profile,edit_profile , upload_report,delete_report,doctor_view_profile

urlpatterns = [
    path("create/" , create_profile , name="create_profile"),
    path("edit/",edit_profile,name="edit_profile"),
    path("upload-report/",upload_report,name="upload_report"),
    path("delete-report/<int:report_id>/",delete_report,name="delete_report"),
    path("doctor/profile/<uuid:uuid>/", doctor_view_profile, name="doctor_view_profile"),
]