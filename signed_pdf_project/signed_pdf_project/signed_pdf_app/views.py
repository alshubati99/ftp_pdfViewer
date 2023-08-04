from django.shortcuts import render, get_object_or_404
import os
from django.http import HttpResponse, Http404
from .models import FilesAdmin
from django.conf import settings

def home(request):
    context = {'file':FilesAdmin.objects.all()}
    return render(request,'signed_pdf_app/home.html', context )

def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(),content_type = "application/adminupload")
            response['Content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
            return response
    raise Http404
  

# from django.http import HttpResponse
# from .models import SignedPDF

# def index(request):
#     if request.method == 'POST':
#         # Handle file upload and signature verification
#         # (You can use libraries like django-forms, cryptography, or pdf2image for these tasks)
#         # Save the uploaded file and signature in the database
#         pass  # Add your code here for handling file upload and signature verification
        
#     signed_pdfs = SignedPDF.objects.all()
#     return render(request, 'index.html', {'signed_pdfs': signed_pdfs})

# def download_pdf(request, pk):
#     signed_pdf = get_object_or_404(SignedPDF, pk=pk)
#     file_path = signed_pdf.file.path
#     with open(file_path, 'rb') as pdf_file:
#         response = HttpResponse(pdf_file.read(), content_type='application/pdf')
#         response['Content-Disposition'] = f'attachment; filename="{signed_pdf.file.name}"'
#         return response
