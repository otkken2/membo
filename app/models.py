from django.conf import settings
from django.db import models
from django.utils import timezone


# PARTS_CHOICES = [
#     ('ボーカル','ボーカル'),('ギター','ギター'),('ベース','ベース'),
#     ('ドラム','ドラム'),('その他打楽器','その他打楽器'),('ピアノ・キーボード','ピアノ・キーボード'),
#     ('シンセ','シンセ'),('作詞作曲','作詞作曲'),('編曲','編曲'),
#     ('DJ','DJ'),('木管楽器','木管楽器'),('金管楽器','金管楽器'),
#     ('その他弦楽器','その他弦楽器'),('民族楽器','民族楽器'),('その他','その他'),
#     ]
# AREA_CHOICES = [
#     ('北海道','北海道'),('青森県','青森県'),('岩手県','岩手県'),('宮城県','宮城県'),('秋田県','秋田県'),
#     ('山形県','山形県'),('福島県','福島県'),('東京都','東京都'),('神奈川県','神奈川県'),('埼玉県','埼玉県'),
#     ('千葉県','千葉県'),('茨城県','茨城県'),('栃木県','栃木県'),('群馬県','群馬県'),('山梨県','山梨県'),
#     ('新潟県','新潟県'),('長野県','長野県'),('富山県','富山県'),('石川県','石川県'),('福井県','福井県'),
#     ('愛知県','愛知県'),('岐阜県','岐阜県'),('静岡県','静岡県'),('三重県','三重県'),('大阪府','大阪府'),
#     ('兵庫県','兵庫県'),('京都府','京都府'),('滋賀県','滋賀県'),('奈良県','奈良県'),('和歌山県','和歌山県'),
#     ('鳥取県','鳥取県'),('島根県','島根県'),('岡山県','岡山県'),('広島県','広島県'),('山口県','山口県'),
#     ('徳島県','徳島県'),('香川県','香川県'),('愛媛県','愛媛県'),('高知県','高知県'),('福岡県','福岡県'),
#     ('佐賀県','佐賀県'),('長崎県','長崎県'),('熊本県','熊本県'),('大分県','大分県'),('宮崎県','宮崎県'),
#     ('鹿児島県','鹿児島県'),('沖縄県','沖縄県'),
#     ]
# GENRE_CHOICES = [
#     ('ポップ','ポップ'),('ロック','ロック'),('エレクトロ/ダンス','エレクトロ/ダンス'),
#     ('R&B','R&B'),('ゴスペル','ゴスペル'),('ソウル','ソウル'),
#     ('ジャズ','ジャズ'),('クラシック','クラシック'),('パンク','パンク'),
#     ('レゲエ','レゲエ'),('メタル','メタル'),('ラテン','ラテン'),
#     ('ファンク','ファンク'),('ブルース','ブルース'),('カントリー','カントリー'),
#     ('フォーク','フォーク'),('アコースティック','アコースティック'),
#     ('アイリッシュ','アイリッシュ'),('インスト','インスト'),('その他','その他'),
# ]





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

    def __str__(self):
        return self.title

    def publish(self):
        self.post_date = timezone.now()
        self.save()