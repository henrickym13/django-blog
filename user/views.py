from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('notice_list')
    else:
        form = CustomCreationForm()
    return render(request, 'register.html', {'form': form})