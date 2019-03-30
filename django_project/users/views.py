from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(task):
    if task.method=='POST':
        form=UserRegisterForm(task.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(task, f'Account created for {username}!')
            return redirect('blog-main')
    else:
        form=UserRegisterForm()
    return render(task, 'users/register.html', {'form':form})
