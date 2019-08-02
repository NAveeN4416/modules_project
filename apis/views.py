from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .model_serializers import UserSerializer, UserMSerializer, UserdetailsSerializer
from users.models import UserDetails
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from collections import OrderedDict

# Create your views here.
		
# ViewSets define the view behavior.
class UserViewSet(viewsets.ViewSet):

	queryset         = User.objects.all()
	serializer_class = UserSerializer


	def list(self,request):
		queryset = User.objects.all()
		serializer = UserSerializer(queryset,many=True)
		return Response(serializer.data)

	def retrieve(self,request,pk=0):
		queryset = User.objects.all()
		queryset = get_object_or_404(queryset,pk=pk)
		serializer = UserSerializer(queryset)
		return Response(serializer.data)


class UserMViewSet(viewsets.ModelViewSet):

	queryset         = User.objects.all()
	serializer_class = UserMSerializer

	send    = {}
	details = {}

	single_record  = False

	send['status']  = 0
	send['message'] = "User Not found!"
	send['data']    = {}

	#==Inherited Methods==

	#Get Users List
	def list(self,request):

		if self.ProcessUsers():
			users = self.userslist
			self.send['status']  = 1
			self.send['message'] = "success"
			self.send['data']    = users

		return Response(self.send)


	#Get Single User
	def retrieve(self,request,pk=0):

		self.single_record = True
		
		try:
			users = User.objects.get(pk=pk)
		except User.DoesNotExist:
			pass
		else:

			self.queryset = users
			if self.ProcessUsers():
				self.send['status']  = 1
				self.send['message'] = "success"
				self.send['data']    = self.userslist

			#Append user prodfile/details
			if self.ProcessUserDetails():
				details  = self.details
				self.send['data']['details'] = details

		return Response(self.send)


	#===New Methods====
	def ProcessUserDetails(self):

		details  = UserDetails.objects.get(user=self.queryset)
		details  = UserdetailsSerializer(details)

		if details:
			self.details = details.data
			return True
		return False


	def ProcessUsers(self):

		users  = self.queryset

		if self.single_record:
			users = UserSerializer(users)
		else:
			users = UserSerializer(users,many=True)

		if users.data:
			self.userslist = users.data
			return True
		return False


#=====================Functions==========================================

