from rest_framework import serializers
from medical_profile.models import MedicalProfile,MedicalReport
from scan_tracking.models import ScanLog
from accounts.models import User

class MedicalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalProfile
        fields = [
            "uuid",
            "full_name",
            "blood_group",
            "allergies",
            "diseases",
            "emergency_contact",
        ]

class MedicalReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalReport
        fields = [
            "id",
            "report_file",
            "uploaded_at"
        ]
class ScanLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanLog
        fields=[
            "ip_address",
            "location",
            "timestamp",
        ]
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "username",
            "email",
            "phone",
            "password",
        ]
    def create(self, validated_data):
        user = user.objects.create_user(
            username = validated_data["username"],
            email = validated_data["email"],
            phone = validated_data["phone"],
            password = validated_data["password"],

        )
        return user