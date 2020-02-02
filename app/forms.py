from django import forms
from app.models import Mailer
from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import time


class MailerForm(forms.ModelForm):
    
    class Meta:
        model = Mailer
        fields = ("to_email", "subject", "message", "delay")
