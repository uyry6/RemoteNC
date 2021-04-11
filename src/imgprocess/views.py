from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImgForm
from .models import IMG
import pathlib
from wand.image import Image as wi
from urllib.request import urlopen

# Create your views here.
def imgprocess_create(request):
    form = ImgForm()
    if request.method == 'POST':
        # print(request.FILES["img"].content_type == 'application/pdf')
        if request.FILES["img"].content_type == 'application/pdf':
            # itemUrl  = 'http://127.0.0.1:8000' + item.img.url
            # response = urlopen(itemUrl)
            # pdfImg  = wi(request.FILES["img"])
            # # pdfImg.convert('png')
            form = ImgForm(request.POST, request.FILES)
        # print(form)
            if form.is_valid():
                pdfFile = request.FILES["img"].save(commit=False)
                print(pdfFile)
                pdfFile.img = wi(file=pdfFile.img, resolution=200)
                pdfFile.save()
    context = {
        'mytxt': 'please upload .png .jpg .pdf only',
        'form': form
    }
    return render(request, "img_upload.html", context)

# imgs = IMG.objects.all()
# for img in imgs:
#     print('http://127.0.0.1:8000' + img.img.url)

def imgprocess_view(request, *args, **kwargs):
    imgs = IMG.objects.all()
    # for item in imgs:
    #     if item.name == 'pdf':
    #         itemUrl  = 'http://127.0.0.1:8000' + item.img.url
    #         response = urlopen(itemUrl)
    #         itemImg  = wi(file=response, resolution=200)
    #         item.img = itemImg.convert('png')
    context = {
        'imgs': imgs,
    }
    return render(request, "img.html", context)
