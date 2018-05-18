from django.db import models

# Create your models here.
class App(models.Model):
	log = models.CharField(max_length=256)
    url = models.URLField()
    flag = models.BooleanField()

	def __str__(self):
		return self.name
