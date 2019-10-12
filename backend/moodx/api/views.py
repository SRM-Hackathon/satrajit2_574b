from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from api.decorators.response import JsonResponseDecorator
import base64
import os
import time


@method_decorator(JsonResponseDecorator, name='dispatch')
class SuggestView(View):
    def post(self, request):
        print(request.POST)
        image = request.POST.get('image')
        image = str(image)[22:]
        image = base64.b64decode(image)
        curr_time = time.time()
        save_path = os.path.join(settings.MEDIA_ROOT, f'image_{curr_time}.png')

        with open(save_path, 'wb+') as f:
            f.write(image)

        print(f'Received: {save_path}')
        return {'message': f'Uploaded {save_path}'}
