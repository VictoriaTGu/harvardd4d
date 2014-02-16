from django.contrib import admin
import accounts.models

# Register your models here.
admin.site.register(accounts.models.UserRole)
admin.site.register(accounts.models.UserProfile)
