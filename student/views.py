from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .forms import CustomUserCreationForm
from student.models import CustomUser
from django.views import generic
from.models import CustomUser


# Create your views here.
class StudentListView(ListView):

    model = CustomUser
    template_name = "student/home.html"
    context_object_name = 'students'


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm

    success_url = reverse_lazy('login')

    template_name = "registration/signup.html"


class StudentDetailView(DetailView):
    model = CustomUser
    template_name = "student/profile.html"
    context_object_name = 'student'
