from django.contrib import admin
from .models import Contact
# Register your models here.

class FormAdmin(admin.ModelAdmin):
	list_display = ['name', 'address']
	list_filter = ['name','address']


admin.site.register(Contact, FormAdmin)