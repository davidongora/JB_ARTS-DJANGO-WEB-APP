from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from typing import Union, Any
from django.contrib.auth import logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth import login

from jb1 import settings

# Create your views here.
    
    
# USER REGISTRATION


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:   
            if User.objects.filter(username=username).exists():
                messages.info(request, 'USERNAME TAKEN')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'EMAIL EXISTS')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,
                                                last_name=last_name,
                                                username=username, 
                                                email=email,
                                                password=password1, 
                                                )
                user.save()
                user.is_active = False
                messages.info(request, 'Account has been successfully created.We have sent you a confirmation Email.Please confirm your Email in order to verify your account.')
                return redirect('signin')
        else:
            messages.info(request, 'PASSWORDS NOT MATCHING')
            return redirect('register')
        
    else:
        return render(request, 'register.html')
      
    # USER LOGIN 


def signin(request: Any) -> Union[HttpResponseRedirect, 
                                  HttpResponsePermanentRedirect, HttpResponse]:
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            first_name = user.first_name
            return redirect('/', {'first_name': first_name})
        else:
            messages.info(request, 'INVALID CREDENTIALS')
            return redirect('signin')
        
    else:
        return render(request, 'signin.html')
    
    # USER LOGOUT
 
    
def signout(request):
    logout(request)
    messages.info(request, 'LOGGED OUT SUCCESSFULY')
    return redirect('signin')

# EMAIL VERIFIACTION


def send_verification_email(request, user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    subject = 'Activate Your Account'
    message = render_to_string('email_verification.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': uid,
        'token': token,
    })
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return HttpResponse('Activation link is invalid!')
