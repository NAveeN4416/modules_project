from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import UserDetails

# Serializers define the API representation.
class UserSerializer(serializers.Serializer):

	email        = serializers.EmailField(max_length=254)
	username     = serializers.CharField(max_length=150)
	first_name   = serializers.CharField(max_length=30)
	last_name    = serializers.CharField(max_length=150)
	is_staff     = serializers.IntegerField()
	is_active    = serializers.IntegerField()
	date_joined  = serializers.DateTimeField()

	# class Meta:
	# 	model = User
	# 	fields = ['username','first_name','last_name','email','is_staff','is_active','date_joined','url'] #'__all__' #

# Serializers define the API representation.
class UserMSerializer(serializers.ModelSerializer):

	class Meta:
	 	model = User
	 	fields = ['username','first_name','last_name','email','is_staff','is_active','date_joined','url'] #'__all__' #