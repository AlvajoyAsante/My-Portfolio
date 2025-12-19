from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    site_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    linkedin_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    kofi_link = models.URLField(blank=True, null=True)
    youtube_channel_id = models.CharField(max_length=100, blank=True, null=True)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Personal Info"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
