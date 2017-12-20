from django import forms
from django.forms import ModelForm
from .models import Captcha

class CaptchaForm(forms.ModelForm):

    class Meta:
        model = Captcha
        fields = [
            "captcha_text"
        ]




