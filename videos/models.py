from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Video(models.Model):
	video_title = models.CharField(max_length=900)
	pub_date = models.DateTimeField('date published')
	video_url = models.CharField(max_length=900)

	def __str__(self):
		return self.video_title

