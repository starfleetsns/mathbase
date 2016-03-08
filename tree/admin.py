from django.contrib import admin
from tree.models import Node, Link

# Register your models here.
admin.site.register(Node)
admin.site.register(Link)

class LinkAdmin(admin.ModelAdmin):
	date_hierarchy = 'added'
