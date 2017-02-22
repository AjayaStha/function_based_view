from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=30)
	email = models.EmailField()
	mobile = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name