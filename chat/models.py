from django.db import models

# Create your models here.
class ChatLog(models.Model):
    room_name = models.CharField(max_length=100)
    handle = models.CharField(max_length=100)
    message = models.TextField()
    date = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'ChatLog(【{}】by【{}】,created_at:{}'.format(self.room_name,self.handle,self.date)