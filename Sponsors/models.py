from django.db import models

# Create your models here.
class Sponsor(models.Model):
	name = models.CharField(max_length=256)
	details = models.TextField()
	pic = models.ImageField(upload_to='Sponsors')
	contact = models.IntegerField()
	website = models.URLField(blank=True)
	spons_type = models.TextField()
	flag = models.BooleanField()

	def __str__(self):
		return self.name


