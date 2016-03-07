from django.shortcuts import render
from django.views.generic.detail import DetailView
from models import Node

# Create your views here.
class ShowNode(DetailView):
	model = Node
#	template_name = 'tree/node_detail.html'	
