from django.contrib import admin
from .models import PersonalInfo

# Register your models here.
@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'occupation')


