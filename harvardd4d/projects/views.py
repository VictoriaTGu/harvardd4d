from django.shortcuts import render
from projects.models import Partner

# Create your views here.
def index(request):
    context = {}
    return render(request, 'projects/index.html', context)

def about(request):
        context = {}
        return render(request, 'projects/about.html', context)

def titw(request):
    context = {}
    return render(request, 'projects/titw.html', context)

def idhack(request):
    context = {}
    return render(request, 'projects/idhack.html', context)

def ttp(request):
    context = {}
    return render(request, 'projects/ttp.html', context)

def discuss(request):
    context = {}
    return render(request, 'projects/discuss.html', context)

def events(request):
    context = {}
    return render(request, 'projects/events.html', context)

def external(request):
    context = {}
    return render(request, 'projects/external.html', context)

def partners(request):
    context = {}
    return render(request, 'projects/partners.html', context)

def sponsors(request):
    context = {}
    return render(request, 'projects/sponsors.html', context)

def past_sponsors(request):
    context = {}
    return render(request, 'projects/past_sponsors.html', context)

def contact_us(request):
    context = {}
    return render(request, 'projects/contact_us.html', context)
#
#def partners(request):
#    partners = Partner.objects.all()
#    context = {'partners': partners}
#    return render(request, 'projects/partners.html', context)
