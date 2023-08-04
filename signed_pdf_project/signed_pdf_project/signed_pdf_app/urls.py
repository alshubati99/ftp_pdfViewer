# signed_pdf_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/<int:pk>/', views.download_pdf, name='download_pdf'),
    # Add other URL patterns for anti-bot verification if needed
]
