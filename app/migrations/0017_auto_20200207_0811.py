# Generated by Django 2.2.9 on 2020-02-06 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20200206_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoundFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sounds', models.FileField(null=True, upload_to='uploads', verbose_name='音源')),
            ],
        ),
        migrations.RemoveField(
            model_name='postcontent',
            name='sound',
        ),
        migrations.AddField(
            model_name='postcontent',
            name='sound',
            field=models.ManyToManyField(to='app.SoundFile', verbose_name='音源'),
        ),
    ]
