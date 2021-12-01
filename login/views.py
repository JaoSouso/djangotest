from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login


# Create your views here.
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect(request, '/home')

    return render(request, 'login.html')