from django.shortcuts import render
from django.views import View

class Index(View):
	template = 'ui/index.html'

	def get(self, request):
		return render(request, self.template)

class Insults(View):
	template = 'ui/insults.html'
	def get(self, request):
		return render(request, self.template)