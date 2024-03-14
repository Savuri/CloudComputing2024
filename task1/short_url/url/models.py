from django.db import models

class ShortenedUrl(models.Model):
    origin = models.URLField()
    shortening = models.URLField()

    def __str__(self):
        return f'[{self.origin} - {self.shortening}]'
