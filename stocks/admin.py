from django.contrib import admin
from .models import Company, History

# Register your models here.

admin.site.register([Company, History])