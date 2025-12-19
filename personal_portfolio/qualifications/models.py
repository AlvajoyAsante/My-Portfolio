from django.db import models
from django.db.models import F

# Create your models here.
class Qualification(models.Model):
    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('education', 'Education'),
        ('school', 'School Activities'),
        ('certifications', 'Certifications'),
    ]

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    # date_range field removed, using property instead
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    link = models.URLField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank for 'Present'")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [F('end_date').desc(nulls_first=True), '-start_date']

    def __str__(self):
        return f"{self.title} - {self.subtitle}"

    @property
    def date_range(self):
        if not self.start_date:
            return ""
        
        start_str = self.start_date.strftime('%b %Y')
        
        if self.end_date:
            if self.start_date == self.end_date:
                return start_str
            end_str = self.end_date.strftime('%b %Y')
        else:
            end_str = "Present"
            
        return f"{start_str} - {end_str}"

