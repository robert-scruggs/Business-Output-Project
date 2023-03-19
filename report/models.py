from django.db import models

# Create your models here.
class SearchLog(models.Model):
    url = models.CharField(max_length=255)
    iswp = models.BooleanField(default=False)
    search_time = models.DateTimeField(auto_now=True)


