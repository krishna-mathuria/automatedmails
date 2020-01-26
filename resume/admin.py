from django.contrib import admin
from resume.models import PersonalData, Files
# Register your models here.


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone')
    search_fields = ('title', 'userid')


admin.site.register(PersonalData)
admin.site.register(Files)
