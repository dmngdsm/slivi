from django.shortcuts import render, redirect, render_to_response
from django.template import loader
import requests
from .forms import CaptchaForm
from .models import Captcha
import os
import shutil
from django.core.files.base import File
from django.core.files.uploadedfile import SimpleUploadedFile


from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

# Create your views here.


def get(request):

    template_name='slivi/index.html'
    template = loader.get_template(template_name)

    # Create static image to save content to
    filename = 'slivi/static/slivi/test.jpg'

    # Create the same image but in media
    filename2 = 'slivi/media/test.jpg'

    #  First get Captcha image
    img_data = requests.get('https://www.dnes.bg/lib/ibgws/ibgws_comments/validate/code.php').content

    # and save to local static file
    with open(filename, 'wb') as handler:
        handler.write(img_data)

    # save to image in media folder
    with open(filename2, 'wb') as handler:
        handler.write(img_data)

    #  Load the View
    if request.method == 'POST':
        os.rename('slivi/media/test.jpg', 'slivi/media/kur.jpg')
        form = CaptchaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)


            t = Captcha.objects.latest("id")
            filename3 = 'slivi/media/' + t.captcha_text + '.jpg'
            shutil.copyfile('slivi/media/kur.jpg', filename3)
            t.captcha_image = filename3
            t.save()


            return render(request,template_name, {'form':form})
    else:
        form = CaptchaForm()
    return render(request, template_name, {'form':form})






























