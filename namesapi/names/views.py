# apiviews
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Name
from .serializers import NameSerializer

class NameList(APIView):
    def get(self, request):
        names = Name.objects.all()
        data = NameSerializer(names, many=True).data
        print("data is ", data)
        return Response(data)

# class NameList(generics.ListCreateAPIView):
#     queryset = Name.objects.all()
#     serializer_class = NameSerializer

def names_list(request):
    names = Name.objects.all()
    data = {"results": list(names.values("first_name", "last_name"))}
    return JsonResponse(data)



class NameDetail(APIView):
    def get(self, request, pk):
        name = get_object_or_404(Name, pk=pk)
        data = NameSerializer(name).data
        return Response(data)