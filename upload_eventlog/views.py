from django.core import validators
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat


def upload_page(request):
    # if user wants to upload a file
    if request.method == 'POST' and request.FILES['upload_file']:
        # get file from form
        file = request.FILES['upload_file']
        validator = FileExtensionValidator(['csv', 'xes'])
        try:
            validator(file)
        except ValidationError as error:
            return render(request, 'upload_page.html', {'error': error})
        # create new FileSystemStorage
        fs = FileSystemStorage()
        # save file and get filename
        filename = fs.save(file.name, file)
        # get file url
        file_url = fs.url(filename)
        # return file url
        return render(request, 'upload_page.html', {'file_url': file_url})
    # return empty page
    return render(request, 'upload_page.html')
