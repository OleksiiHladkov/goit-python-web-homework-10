from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import RegisterForm


class RegisterView(View):
    form_class = RegisterForm
    template_name = "users/signup.html"


    def dispatch(self, request, *args: Any, **kwargs: Any):
        if request.user.is_authenticated:
            return redirect(to="quotes:main")
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
    

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Congratulate {username}. Your account has been successfully created.")
            return redirect(to="users:login")
        return render(request, self.template_name, {"form": form})