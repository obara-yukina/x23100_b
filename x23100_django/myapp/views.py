from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def showUsers(request):
    user = User.objects.all()
    context = {
        'user':user,
        'count':user.count,
    }

    return render(request, 'myapp/users.html', context)
