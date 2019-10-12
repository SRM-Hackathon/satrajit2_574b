from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from api.decorators.response import JsonResponseDecorator
import base64
import os


@method_decorator(JsonResponseDecorator, name='dispatch')
class SuggestView(View):
    def get(self, request):
        image_str = request.GET.get('image')
        imgdata = base64.b64decode(image_str)
        filepath = os.path.join(settings.MEDIA_ROOT, 'some_image.jpg')

        with open(filepath, 'wb') as f:
            f.write(imgdata)

        return {'message': f'Uploaded {filepath}'}

    def post(self, request):
        print(request.POST)
        print(request.FILES)
        image = request.FILES.get('image')
        print(f'Received: {image}')
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)

        return {'message': f'Uploaded {filename}'}
