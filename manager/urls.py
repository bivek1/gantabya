from django.urls import path
from .import views

app_name = 'manager'

urlpatterns = [
    path('dashboard', views.dashBoard, name = 'dashboard'),
    path('courses', views.news, name = "news"),
    path('students', views.studentList, name = "student"),
    path('delete-student/<int:id>', views.deleteStudent, name = "deleteStudent"),
    path('details-student/<int:id>', views.studentProfile, name = "studentProfile"),
    path('allCourse', views.allNews, name="allNews"),
    path('deleteCourse/<int:id>', views.deleteNews, name = "deleteNews"),
    path('update-Course/<int:id>', views.updateNews, name = "updateNews"),
    path('category', views.CategoryView, name = "category"),
    path('delete-category/<int:id>', views.deleteCategory, name = "deleteCategory"),
    path('user-list', views.userList, name = "userList"),
    path('delete-user/<int:id>', views.deleteUser, name = "deleteUser"),
    path('check-password', views.checkPassword, name = "checkPassword"),
    path('Course-selected/<str:str>', views.cnews, name = "cNews"),
    path('applied-scholorship', views.appliedScholor, name = "appliedScholor"),
    path(
        'kyc-verification-request-list', views.kycView, name="kyc"
    ),
    path(
        'verify-kyc-now/<int:id>', views.verifyView, name = "verify"
    ),
    path(
        'reject-kyc-now/<int:id>', views.rejectView, name = "rejectNow"
    ),
    path('KYC-VERIFICATION-DETAILS/KYCVERIFIEDMETHOD-121/<int:id>', views.kycVerification, name="kycVerification"),
]
