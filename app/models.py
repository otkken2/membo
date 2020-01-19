from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class PostContent(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)
    actv_area = models.CharField(max_length=10)
    mypart = models.CharField(max_length=50)
    yourparts = models.CharField(max_length=50)
    favorite = models.TextField()
    sound = models.FileField(upload_to='uploads')

    def publish(self):
        self.published_data = timezone.now()
        self.save()