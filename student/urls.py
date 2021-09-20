from django.urls import path
from student.views import SignUpView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup")
]
