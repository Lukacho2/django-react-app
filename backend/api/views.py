from django.shortcuts import render
from .models import Group

# Create your views here.
def index(request):
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'api/index.html', context)
