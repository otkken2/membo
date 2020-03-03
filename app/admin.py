from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Instrument)
admin.site.register(Prefecture)
admin.site.register(Genre)
admin.site.register(PostContent)
admin.site.register(DaysOfTheWeek)