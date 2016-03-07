from django.db import models

# Create your models here.
class Node(models.Model):
	name = models.TextField()
	text = models.TextField()
	parent = models.ManyToManyField('Node', null=True, blank=True, related_name='children')

	def __str__(self):
		return str(self.name)

class Link(models.Model):
	name = models.TextField()
	description = models.TextField()
	link = models.URLField(max_length=500)
	nodes = models.ManyToManyField('Node', related_name='links')

	def __str__(self):
		return str(self.name) + " - " + str(self.link)