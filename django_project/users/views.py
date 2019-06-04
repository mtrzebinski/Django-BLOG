from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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
    if task.method=='POST':
        user_form = UserUpdateForm(task.POST, instance=task.user)
        profile_form = ProfileUpdateForm(task.POST, task.FILES, instance=task.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(task, f'Your account has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=task.user)
        profile_form = ProfileUpdateForm(instance=task.user.profile)
    context = {'user_form':user_form,'profile_form':profile_form}
    return render(task, 'users/profile.html', context)
