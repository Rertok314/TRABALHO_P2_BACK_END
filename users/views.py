from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import CustomUser

class UserListView(ListView):
    model = CustomUser
    template_name = "users/user_list.html"
    context_object_name = "users"

class UserCreateView(CreateView):
    model = CustomUser
    fields = ["username", "email", "role", "password"]
    template_name = "users/user_form.html"
    success_url = reverse_lazy("user_list")

class UserUpdateView(UpdateView):
    model = CustomUser
    fields = ["username", "email", "role"]
    template_name = "users/user_form.html"
    success_url = reverse_lazy("user_list")

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = "users/user_confirm_delete.html"
    success_url = reverse_lazy("user_list")
