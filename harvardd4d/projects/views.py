from django.shortcuts import render
from projects.models import Partner

# Create your views here.
def index(request):
	context = {}
	return render(request, 'projects/index.html', context)

def partners(request):
	partners = Partner.objects.all()
	context = {'partners': partners}
	return render(request, 'projects/partners.html', context)
