from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(task):
    if task.method=='POST':
        form=UserRegisterForm(task.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(task, f'Your account has been created!')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(task, 'users/register.html', {'form':form})

@login_required
def profile(task):
    return render(task, 'users/profile.html')
