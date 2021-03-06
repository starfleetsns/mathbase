from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Node(models.Model):
	name = models.TextField()
	text = models.TextField()
	parent = models.ForeignKey('Node', null=True, blank=True, related_name='children')
	#deleted = models.BooleanField(editable=False, default=False)

	def __str__(self):
		return str(self.name)

class Link(models.Model):
	name = models.TextField()
	description = models.TextField()
	link = models.URLField(max_length=500)
	added = models.DateField(auto_now_add=True)
	nodes = models.ManyToManyField('Node', related_name='links')
	#deleted = models.BooleanField(editable=False, default=False)
	tags = models.ManyToManyField('Tag', related_name='links')

	def __str__(self):
		return str(self.name) + " - " + str(self.link)

class Tag(models.Model):
	name = models.CharField(max_length=80)
	
	def __str__(self):
		return str(self.name)
