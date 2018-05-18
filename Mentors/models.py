from django.db import models

class Mentor(models.Model):
    name = models.CharField(max_length=256)
    contact = models.IntegerField()
    email = models.CharField(max_length=256)
    detail = models.TextField()
    description = models.TextField()
    profile_pic = models.ImageField(upload_to='Mentors')
    flag = models.BooleanField()

    def __str__(self):
        return self.name
