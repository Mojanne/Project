from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

#We use Django's default form
#if its a POST request validate it if not create blank form
#form.cleaned_data returns a dictionary of validated form input fields and their values, where string primary keys are returned as objects
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For You, Dear {username}!')
            return redirect('blog-homepage')
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {'form': form})



