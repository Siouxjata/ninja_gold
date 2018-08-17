from django.db import models

class Dojo(models.Model):
	name = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	desc = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Ninjas(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	dojo = models.ForeignKey(Dojo, related_name="ninjas")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __repr__(self):
		return (self.first_name)
