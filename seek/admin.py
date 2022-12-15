from django.contrib import admin
from .models import User,Person


admin.site.site_header="Seek Adminastration"
admin.site.site_title="Admin-Dashboard"
admin.site.index_title="Seek Admin-Dashboard"
# Register your models here.
admin.site.register(User)
admin.site.register(Person)
