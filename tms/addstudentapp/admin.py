from django.contrib import admin
from . models import Studentregistration, Payment, Attendence, Result
# Register your models here.
admin.site.register(Studentregistration)
admin.site.register(Payment)
admin.site.register(Attendence)
admin.site.register(Result)
