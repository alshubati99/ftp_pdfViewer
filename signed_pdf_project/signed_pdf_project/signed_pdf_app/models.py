from django.db import models

# Create your models here.
# signed_pdf_app/models.py

# from django.db import models

# class SignedPDF(models.Model):
#     file = models.FileField(upload_to='pdf_files/')
#     signature = models.TextField()
#     uploaded_at = models.DateTimeField(auto_now_add=True)
class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to = 'media')
    title = models.CharField(max_length = 50)
    def __str__(self):
        return self.title

