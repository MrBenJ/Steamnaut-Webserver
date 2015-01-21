from django.contrib import admin
from videos.models import Video
# Register your models here.


class VideoAdmin(admin.ModelAdmin):
	fields = ['video_title', 'pub_date', 'video_url']
	list_display = ('video_title', 'pub_date', 'video_url')

admin.site.register(Video, VideoAdmin)
