from django.utils import timezone
from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse ,JsonResponse
#from .forms import UserRegistration
#from .models import UserDetails
import json
from django.contrib.auth.models import User
from users import constants as C
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.sessions.models import Session
from django.contrib import messages

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils import six
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db.models import Q
from django.conf import settings

from django.db import IntegrityError, transaction, DatabaseError

from core_modules.decors import Set_RequestObject, Check_Login
#==================================Views START================================================



def Index(request):
	return render(request,'dashboard/index.html')


def TermsConditions(request):
	return render(request,'dashboard/terms_conditions.html')