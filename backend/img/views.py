from django.shortcuts import render

# models
from .models import Images
from .serializers import ImagesSerializer
# Create your views here.

# forms
from .forms import UploadFileForm

# rest_framework
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response



class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

@api_view(['POST'])
def save_img(request):
    if request.method == 'POST':
        form = 
        if form.is_valid()
        