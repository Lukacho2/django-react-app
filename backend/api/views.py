from django.shortcuts import render
from .models import Group, User

# Create your views here.
def index(request):
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'api/index.html', context)

def my_profile(request, pk):
    user = User.objects.get(id=pk)

    f_name = user.firstname
    l_name = user.lastname
    description = user.description
    registered_in = user.registered_in
    groups = user.groups.all()

    # Prepare context
    context = {
        'firstname': f_name,
        'lastname': l_name,
        'description': description,
        'registered_in': registered_in,
        'groups': groups
    }

    return render(request, 'myprofile.html', context)