from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.edit import FormView

from registration.backends.simple.views import \
    RegistrationView as BaseRegistrationView
from registration import signals

from .forms import UserCreationForm, CompanyCreationForm, PasswordResetForm

from apps.users.models import User
from apps.companies.models import *


class UserRegistrationView(BaseRegistrationView):
    template_name = 'registration/registration_consumer.html'
    form_class = UserCreationForm

    def register(self, request, **cleaned_data):
        email, password = cleaned_data['email'], cleaned_data['password1']
        User.objects.create_user(email, password)

        new_user = authenticate(username=email, password=password)
        login(request, new_user)
        signals.user_registered.send(
            sender=self.__class__,
            user=new_user,
            request=request
            )
        return new_user

    def get_success_url(self, request, user):
        return '/dashboard/'


class CompanyRegistrationView(BaseRegistrationView):
    template_name = 'registration/registration_company.html'
    form_class = CompanyCreationForm

    def register(self, request, **cleaned_data):
        email, password, name = cleaned_data['email'], \
            cleaned_data['password1'], cleaned_data['name']

        User.objects.create_user(email, password)

        # login the new user
        new_user = authenticate(username=email, password=password)
        login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
            user=new_user, request=request)

        # create the institute and associate it with the newly created user
        company = Company.objects.create(name=name)
        group = CompanyGroup.objects.create(
            name='Administrators', company=company)
        CompanyUser.objects.create(
            user=new_user, company=company, group=group,
            is_owner=True, is_superuser=True, is_default=True)

        return new_user

    def get_success_url(self, request, user):
        return '/dashboard/'


class PasswordResetView(FormView):
    template_name = 'registration/password_reset_frm.html'
    form_class = PasswordResetForm
    success_url = 'registration_password_reset_confirm'

    def get(self, request, *args, **kwargs):
        # Pass request to get_form_class and get_form for per-request
        # form control.
        form = self.get_form(self.form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        if form.is_valid():
            # Pass request to form_valid.
            return self.form_valid(request, form)
        else:
            return self.form_invalid(form)

    def form_valid(self, request, form):
        user = self.user
        user.update_key()
        return redirect(self.success_url)
