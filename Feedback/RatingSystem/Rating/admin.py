from django.contrib import admin
from .models import Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ('good','average','bad','date')
    list_filter = ('date',)

admin.site.register(Rating, RatingAdmin)