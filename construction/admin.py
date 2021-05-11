from django.contrib import admin
from .models import Site_User, Construction_Site, Transaction

admin.site.register(Site_User)
admin.site.register(Construction_Site)
admin.site.register(Transaction)
