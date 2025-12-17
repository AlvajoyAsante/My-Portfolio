from django.contrib import admin
from .models import Qualification

# Register your models here.
@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'category', 'start_date', 'end_date')
    list_filter = ('category',)
    search_fields = ('title', 'subtitle')

