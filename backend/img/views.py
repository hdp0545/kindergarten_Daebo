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
            instance = Images(image=request.FILES['image']) # 감자ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ감쟈ㅑㅑㅑㅑㅑ 대홍단 가암자 ~ 
            instance.save()
            print(instance.image.url)
            print(instance.image.name)
            context = {
                'result' : 'True',
                'message' : '파일을 업로드 하였습니다.',
                'path' : instance.image.url
            }
            return Response(context, status=status.HTTP_200_OK)
    else:
        form = UploadFileForm()
    return Response(context, status=status.HTTP_400_BAD_REQUEST)