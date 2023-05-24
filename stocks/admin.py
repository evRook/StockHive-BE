from django.contrib import admin
from .models import CompanyInfo, History, UserAcct, UserAcctManager, UserFavorites
from . import models
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CompanyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(models.CompanyInfo, CompanyAdmin)

admin.site.register(UserAcct)
admin.site.register(History)
admin.site.register(UserFavorites)
