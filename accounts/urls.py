from django.urls import path
from .views import register_view , login_view ,logout_view,dashboard,admin_panel

urlpatterns = [
    path("register/",register_view,name="register"),
    path("login/",login_view,name="login"),
    path("logout/",logout_view,name="logout"),
    path("dashboard/",dashboard,name="dashboard"),
    path("admin-panel/",admin_panel,name="admin_panel"),
]