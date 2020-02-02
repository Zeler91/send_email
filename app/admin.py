from django.contrib import admin
from app.models import Mailer

@admin.register(Mailer)
class mailerAdmin(admin.ModelAdmin):
    pass
