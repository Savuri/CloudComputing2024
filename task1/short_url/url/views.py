from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.core.validators import URLValidator
from . import forms
from . import models

import binascii

def error(request):
    return render(request, 'error.html')

def home(request):
    generated_url = None
    if request.method == 'POST':
        form = forms.ShortenUrlCreateForm(request.POST, request.FILES)
        if form.is_valid():
            generated = form['origin'].value()
            for _ in range(100):
                generated = binascii.crc32(str(generated).encode('utf8'))
                if not models.ShortenedUrl.objects.filter(shortening=str(generated)).exists():
                    break
            else:
                return redirect('url:error') 
            shortened_url = form.save(commit=False)
            shortened_url.shortening = generated
            shortened_url.save()
            generated_url = f"{request.scheme}://{request.get_host()}/{generated}"
    elif request.method == 'GET':
        form = forms.ShortenUrlCreateForm()
        
    return render(request, 'home.html', {'form': form, 'generated': generated_url})

def redirect_by_shortening(request, short_url):
    url = models.ShortenedUrl.objects.filter(shortening=short_url)
    if url.exists():
        return redirect(url.first().origin)

    return HttpResponseNotFound("<h1> No shortening </h1>")