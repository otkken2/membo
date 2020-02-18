from django.conf import settings
from django.db import models
from django.utils import timezone



# Create your models here.
class Instrument(models.Model):
    instname = models.CharField('パート',max_length=50)
    def __str__(self):
        return self.instname

class Prefecture(models.Model):
    prefname = models.CharField('都道府県',max_length=50)
    def __str__(self):
        return self.prefname

class Genre(models.Model):
    genrename = models.CharField('ジャンル',max_length=50)
    def __str__(self):
        return self.genrename

# class SoundFile(models.Model):
#     sounds = models.FileField('音源',upload_to='uploads',null=True)

# class Member(models.Model):
#     name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


def get_media_sound_path(instance,filename):
    return 'uploads/{0}/{1}'.format(instance.author.id,filename)

class PostContent(models.Model):

    DAYS_CHOICE=[
        ('土日','土日'),
        ('平日','平日'),
        ('指定なし','指定なし'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('タイトル',max_length=50)
    sound = models.FileField('音源',upload_to=get_media_sound_path,null=True)
    text = models.TextField('本文')
    post_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now_add=True)
    active_area = models.ManyToManyField(Prefecture,verbose_name='活動エリア（都道府県）',null=True)
    mypart = models.ManyToManyField(Instrument,verbose_name='投稿者のパート',null=True,related_name='mypart')
    recruite_part = models.ManyToManyField(Instrument,verbose_name='募集パート',null=True,related_name='recruite_part')
    genre = models.ManyToManyField(Genre,verbose_name='ジャンル',null=True)
    favorite = models.TextField('好きなアーティスト',null=True)
    days_of_theweek = models.CharField('活動の曜日',max_length=50,null=True,choices=DAYS_CHOICE)

    def __str__(self):
        return self.title

    def publish(self):
        self.post_date = timezone.now()
        self.save()