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
    date_range = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    link = models.URLField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank for 'Present'")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [F('end_date').desc(nulls_first=True), '-start_date']

    def __str__(self):
        return f"{self.title} - {self.subtitle}"

