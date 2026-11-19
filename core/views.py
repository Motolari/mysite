from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Media
from .forms import MediaForm

def home(request):
    items = Media.objects.order_by('-uploaded_at')
    return render(request, 'core/home.html', {'items': items})

def upload(request):
    form = MediaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'core/upload.html', {'form': form})