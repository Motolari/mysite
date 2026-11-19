from django.db import models

# Create your models here.
class Media(models.Model):
    TYPES = [('image', 'Image'), ('video', 'Video'), ('audio', 'Audio')]
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=10, choices=TYPES)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title