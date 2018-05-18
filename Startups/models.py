from django.db import models

# Create your models here.
class Startup(models.Model):
	name = models.CharField(max_length=256)
	email = models.CharField(max_length=256)
	pic = models.ImageField(upload_to='Startups')
	contact = models.IntegerField()
	founder = models.CharField(max_length=256)
	address = models.TextField()
	flag = models.BooleanField()

	def __str__(self):
		return self.name
