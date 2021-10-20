from django.contrib import admin
from .models import Site_User, Construction_Site, Transaction, AttendenceReport, Worker

admin.site.register(Site_User)
admin.site.register(Construction_Site)
admin.site.register(Transaction)
admin.site.register(AttendenceReport)
admin.site.register(Worker)
