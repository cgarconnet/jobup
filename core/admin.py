from django.contrib import admin

# Register your models here available in the admin
import core.models as coremodels

admin.site.register(coremodels.UserProfile)
