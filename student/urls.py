from django.urls import path
from django.contrib.auth import views
from .forms import UserLoginForm, ChangePasswordForm
from student.views import SignUpView, StudentDetailView, StudentListView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path(
        'login/',
        views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm
        ),
        name='login'
    ),
    path(
        'password_change/', views.PasswordChangeView.as_view(
            template_name='registration/password_change_form.html',
            form_class=ChangePasswordForm,
            # success_url='accounts/password_change_done'

        ), name='change_password'),
    path('std_profile/<int:pk>/', StudentDetailView.as_view(), name="std_profile"),
    path('all_students/', StudentListView.as_view(), name="student_list"),
]
