from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import FormView
from .forms import FileFieldForm

import time
from PIL import Image, ImageOps
import os

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'img_processing/upload_image.html'  # Replace with your template.
    success_url = 'uploaded_image.html'  # Replace with your URL or reverse().

    def get(self, request, *args, **kwargs):
        form = FileFieldForm()
        context = {'form': form}
        return render(request, 'img_processing/upload_image.html', context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('upload_files_here')

        if form.is_valid():
            fs = FileSystemStorage()
            context = {}
            filenames = []
            i = 0
            for f in files:
                filename = fs.save(f.name, f)
                uploaded_file_url = fs.url(filename)

                os.chdir(r'/home/mohit/Web_Interface_Image_Processing/Web_Interface_IP/SIH/img_processing')
                im = Image.open(f.name)
                im_mirror = ImageOps.mirror(im)
                im_mirror.save('static/'+filename)
                filenames.append(f.name)

            context.update({'filenames': filenames,})


            return render(request, 'img_processing/uploaded_image.html', context)
        else:
            return super(FileFieldView, self).form_invalid(form)


def index(request):
    return render(request, 'img_processing/index.html')

def uploaded_image(request):
    return render(request, 'img_processing/uploaded_image.html')

def download(request,file_name):
    file_path = static +'/'+ file_name
    file_wrapper = FileWrapper(file(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str(file_name)
    return response

def custom_image(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        return render(request, 'img_processing/uploaded_image.html')
    # 'uploaded_file_url': uploaded_file_url
    return render(request, 'img_processing/upload_image.html')

def approach(request):
    return render(request, 'img_processing/approach.html')
