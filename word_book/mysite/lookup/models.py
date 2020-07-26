from django.db import models

# Create your models here.
class Entry(models.Model):
	word = models.CharField(max_length = 120) #max_length is required on CharFields
	definition = models.TextField()

	


