from django.urls import path
from .import views

app_name = "customer"

urlpatterns = [
    path('customer-dashboard', views.dashboard, name = "dashboard"),
    path('courses-after-school-nepal', views.courseView, name = "courseStudent"),
    path('verify-your-kyc', views.kycVerify, name = "verify"),
    path('apply-for-scholorship', views.schoView, name = "scho"),
    path("apply-now/<int:id>", views.applyNow, name = "applyNow"),
    path("profile", views.Profile.as_view(), name = "profile"),
    path('customer-profile-pic', views.updatePic, name ="updatePic"),
    path('check-password', views.checkPassword, name = "checkPassword"),
]
