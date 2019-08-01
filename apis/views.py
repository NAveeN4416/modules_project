from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .model_serializers import UserSerializer, UserMSerializer
from users.models import UserDetails
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

# Create your views here.
# ViewSets define the view behavior.
class UserMViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserMSerializer

	# def list(self,request):
	# 	print(self.queryset)
	# 	serializer = UserSerializer(self.queryset,many=True)
	# 	return Response(serializer.data)

	# def retrive(self,request,pk=0):
	# 	queryset = get_object_or_404(self.queryset,pk=pk)
	# 	serializer = UserSerializer(queryset)
	# 	return Response(serializer.data)

class UserViewSet(viewsets.ViewSet):
	
	#serializer_class = UserMSerializer

	def list(self,request):
		queryset = User.objects.all()
		serializer = UserSerializer(queryset,many=True)
		return Response(serializer.data)

	def detail(self,request,pk=0):
		queryset = User.objects.all()
		queryset = get_object_or_404(queryset,pk=pk)
		serializer = UserSerializer(queryset)
		return Response(serializer.data)