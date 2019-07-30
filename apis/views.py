from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .model_serializers import UserSerializer
from users.models import UserDetails
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	# def list(self,request):
 #    	queryset = User.objects.all()
 #    	serializer = UserSerializer(queryset)
 #    	print(serializer.data)
 #    	return Response(serializer.data)

 #    def retrive(self,request,pk=0):
 #    	queryset = User.objects.all()
 #    	queryset = get_object_or_404(queryset,pk=pk)
 #    	serializer = UserSerializer(queryset)
 #    	print(serializer.data)
 #    	return Response(serializer.data)