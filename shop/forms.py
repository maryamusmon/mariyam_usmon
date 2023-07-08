from django import forms
from django.forms import ModelForm
import random

from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail

from root import settings
from shop.cache_function import setKey


class UserRegisterForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user


class ForgotForm(forms.Form):
    email = forms.EmailField()

    def send_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user:
            code = random.randint(10000, 99999)
            setKey(key=user.get().email, value=code, timeout=1000)
            html_message = f"""
            <!DOCTYPE html> 
                <html>
                   <head> 
                      <title>Align Attribute  Example</title> 
                   </head>
                   <body>
                   <h1>Hello {user.get().username}!</h1> 
                   <h2>Your verification code!</h2> 
                   <h1 style="color: red">{code}<h1/>
                   </body>
                </html>
            """
            send_mail(
                subject="Change Password",
                message=None,
                html_message=html_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                auth_user=settings.EMAIL_HOST_USER,
                auth_password=settings.EMAIL_HOST_PASSWORD,
                fail_silently=False
            )
            return user.get().pk
        else:
            return False


class ChangePasswordForm(forms.Form):
    password = forms.CharField(max_length=255)
    confirm_password = forms.CharField(max_length=255)

    def is_valid(self):
        if self.data.get('confirm_password') == self.data.get('password'):
            return super().is_valid()
        else:
            return self.errors

    def save(self, pk):
        user = User.objects.get(pk=pk)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user
