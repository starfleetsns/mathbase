from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.forms.widgets import TextInput
from models import Node, Link

# Create your views here.
class ShowNode(DetailView):
	model = Node
	
	def get_context_data(self, **kwargs):
		context = super(ShowNode, self).get_context_data(**kwargs)
		context['latest_added'] = Link.objects.order_by('-added')[:5]
		# Ed ora prendiamo tutti i padri
		ancestors = [];
		thenode = self.get_object()
		while thenode:
			ancestors.append(thenode)
			thenode = thenode.parent
		context['ancestors'] = reversed(ancestors);
		return context

class NodeCreate(CreateView):
	model = Node
	template_name_suffix = '_create_form'

	def get_initial(self):
		initial = super(NodeCreate, self).get_initial()
		initial['parent'] = get_object_or_404(Node, pk=self.kwargs.get('father'))
		return initial
	
	def get_success_url(self):
		return reverse('tree:ShowNode', kwargs={'pk': self.kwargs.get('father')})
	
class NodeUpdate(UpdateView):
	model = Node
	template_name_suffix = '_update_form'

	def get_success_url(self):
		return reverse('tree:ShowNode', kwargs={'pk': self.get_object().id})


class LinkCreate(CreateView):
	model = Link
	template_name_suffix = '_create_form'

	def get_initial(self):
		initial = super(LinkCreate, self).get_initial()
		initial['nodes'] = Node.objects.filter(pk=self.kwargs.get('next'))
		return initial

	def get_success_url(self):
		return reverse('tree:ShowNode', kwargs={'pk': self.kwargs.get('next')})

class LinkUpdate(UpdateView):
	model = Link
	template_name_suffix = '_update_form'

	def get_success_url(self):
		return reverse('tree:ShowNode', kwargs={'pk': self.kwargs.get('next')})

