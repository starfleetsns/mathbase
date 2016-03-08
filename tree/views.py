from django.shortcuts import render
from django.views.generic.detail import DetailView
from models import Node, Link

# Create your views here.
class ShowNode(DetailView):
	model = Node
	
	def get_context_data(self, **kwargs):
		context = super(ShowNode, self).get_context_data(**kwargs)
		context['latest_added'] = Link.objects.order_by('-added')[:5]
		return context
