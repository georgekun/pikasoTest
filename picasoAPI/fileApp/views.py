from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


from fileApp.models import File
from fileApp.serializers import FileSerializer
from .tasks import process_file

class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = FileSerializer(queryset, many=True)
        return Response(serializer.data)


class FileUploadView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)#получаем сериалайзер
        # Сохраняем объект File с переданными данными
        if serializer.is_valid():
            file_instance = serializer.save()
            # Запускаем задачу Celery для обработки файла
            process_file.delay(file_instance.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

