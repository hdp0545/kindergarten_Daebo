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
        print(request.FILES)
        if form.is_valid():
            instance = Images(image=request.FILES['image']) # image 필수 독학
            instance.save()
            context = {
                'result' : 'True'
                'path' : instance.image.url
            }
            return Response(context, status=status.HTTP_200_OK)
    else:
        form = UploadFileForm()
    return Response(context, status=status.HTTP_200_OK)