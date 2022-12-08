from django.contrib import admin
from .models import employee

class empadmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eadd','email']

admin.site.register(employee,empadmin)
