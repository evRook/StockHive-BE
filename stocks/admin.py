from django.contrib import admin
from .models import Company, History
from . import models
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CompanyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(models.Company, CompanyAdmin)

admin.site.register(History)