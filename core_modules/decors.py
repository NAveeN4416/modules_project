from django.conf  import settings
from django.shortcuts import render,redirect


#Making request obj as GLOBAL ==> decorator
def Set_RequestObject(func):

	def set_obj(request):
		settings.REQUEST_OBJECT = request

	def run_view(*args,**kwargs):
		set_obj(*args,**kwargs)
		return func(*args,**kwargs)

	return run_view


#Checking login ==> decorator
def Check_Login(func):

	def view_func(*args,**kwargs):
		if settings.REQUEST_OBJECT.user.is_authenticated:
			return func(*args,**kwargs)
		return redirect("users:login")

	return view_func