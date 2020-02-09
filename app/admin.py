from django.contrib import admin
from .models import PostContent,Instrument,Prefecture,Genre

# Register your models here.
admin.site.register(Instrument)
admin.site.register(Prefecture)
admin.site.register(Genre)
admin.site.register(PostContent)
# admin.site.register(SoundFile)