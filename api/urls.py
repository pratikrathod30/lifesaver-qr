from django.urls import path
from.views import profile_api,reports_api,scans_api,register_api,login_api,save_location

urlpatterns = [
    path("profile/<uuid:uuid>/",profile_api,name="profile_api"),
    path("reports/<uuid:uuid>/", reports_api, name="reports_api"),
    path("scans/<uuid:uuid>/", scans_api, name="scans_api"),
    path("register/", register_api, name="register_api"),
    path("login/", login_api, name="login_api"),
    path("location/", save_location, name="save_location"),
]