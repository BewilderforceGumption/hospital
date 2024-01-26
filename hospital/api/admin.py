from django.contrib import admin
from .models import Specialization, Patient, Visit, Service, Schedule

# Register your models here.
admin.site.register(Specialization)
admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(Service)
admin.site.register(Schedule)