from django.db import models

class App(models.Model):
	log=models.CharField(max_length=256)
	link=models.URLField(blank=True)
	flag=models.BooleanField()

	def __str__(self):
		return self.name
