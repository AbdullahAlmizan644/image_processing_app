from django.contrib import admin
from .models import Person,Contact,UserImage


admin.site.site_header="Seek Adminastration"
admin.site.site_title="Admin-Dashboard"
admin.site.index_title="Seek Admin-Dashboard"
# Register your models here.
admin.site.register((Person,Contact,UserImage))
