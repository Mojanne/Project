from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

#We use Django's default form
def reguster(request):
    form = UserCreationForm
    return render(request, 'users/registration.html', {'form': form})



