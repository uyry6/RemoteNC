from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImgForm
from .models import IMG

# Create your views here.
def imgprocess_create(request):
    form = ImgForm()
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {
        'mytxt': 'please upload .png .jpg .pdf only',
        'form': form
    }
    return render(request, "img_upload.html", context)


def imgprocess_view(request, *args, **kwargs):
    imgs = IMG.objects.all()
    context = {
        'imgs' : imgs
    }
    return render(request, "img.html", context)
