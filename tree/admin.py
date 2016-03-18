from django.contrib import admin
from tree.models import Node, Link, Tag

# Register your models here.
admin.site.register(Node)
admin.site.register(Link)
admin.site.register(Tag)

class LinkAdmin(admin.ModelAdmin):
	date_hierarchy = 'added'
