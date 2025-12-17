from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    youtube_id = models.CharField(max_length=50, help_text="The ID from the YouTube URL (e.g., dQw4w9WgXcQ)")
    published_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    @property
    def thumbnail_url(self):
        return f"https://img.youtube.com/vi/{self.youtube_id}/mqdefault.jpg"
    
    @property
    def embed_url(self):
        return f"https://www.youtube.com/embed/{self.youtube_id}"
