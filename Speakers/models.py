from django.db import models

# Create your models here.
class Speaker(models.Model):
	name = models.CharField(max_length=256)
	company = models.CharField(max_length=256)
	year = models.IntegerField()
	profile_pic = models.ImageField(upload_to='Speakers')
	email = models.EmailField()
	contact = models.IntegerField()
	flag = models.BooleanField()

	def __str__(self):
		return self.name
		