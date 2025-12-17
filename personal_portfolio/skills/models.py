from django.db import models

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    icon_class = models.CharField(max_length=100, help_text="FontAwesome or Unicons class (e.g. 'uil uil-server-network')")
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Skill Categories"
        ordering = ['order']

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
