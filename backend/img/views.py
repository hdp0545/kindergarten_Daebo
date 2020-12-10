from django.shortcuts import render

# models
from .models import Images
from .serializers import ImagesSerializer
# Create your views here.

# forms
from .forms import UploadFileForm

# rest_framework
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response



class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

@api_view(['POST'])
def save_img(request):
    context = {
                'result' : 'False'    
            }
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Images(file_field=request.FILES['file'])
            instance.save()
            context = {
                'result' : 'True'
            }
            return Response(context, status=status.HTTP_200_OK)
    else:
        form = UploadFileForm()
    return Response(context, status=status.HTTP_200_OK)