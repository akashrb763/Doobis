from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages,auth
import json
from django.http import JsonResponse

from home.forms import CustomUserCreationForm
from home.models import CustomUser

from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode



from datetime import datetime,timedelta
from django.utils import timezone

import os

from cities_light.models import Country, Region, City
# Create your views here.

def home(request):
    return render(request,"index.html")


# Generate token with expiration time
def generate_activation_token(user):
    expiration_time = timezone.now() + timedelta(hours=6)  # Token expires after 1 day
    token = default_token_generator.make_token(user)
    print("gen tocken : ",token)
    return token

# Check if token is valid
def token_is_valid(user, token):
    return default_token_generator.check_token(user, token)

def register(request):
    if request.method == 'POST':
        print("post")

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email=request.POST.get('email')
            phone_number=request.POST.get('phone_number')
            password=request.POST.get('password')
            cpassword=request.POST.get('cpassword')
           
       

            print(email)
            print(password)
            print(cpassword)

            if password == cpassword:
                if CustomUser.objects.filter(email=email).exists():
                    messages.info(request, "email already taken")
                    print(email)
                    return redirect('home:register')
                if CustomUser.objects.filter(email=email, is_active=False).exists():
                    # If the email exists and the associated account is not active
                    user = CustomUser.objects.get(email=email)
                    token = generate_activation_token(user)
                    print(token)
                    send_activation_email(user, token)
                    messages.info(request, "Activation email resent. Please check your email.")
                    return redirect('register:login')
                # if CustomUser.objects.filter(email=email).exists():
                #     messages.info(request, "Email already registered")
                #     print(token)
                #     return redirect('register:register')

                # Create new CustomUser instance
                new_user = CustomUser.objects.create_user(
                    
                    email=email,
                    phone_number=phone_number,
                    username=email.split('@')[0],
                    terms_and_conditions=True,
                    password=password,
                    is_active = False
                )
                token = generate_activation_token(new_user)
                print(token)
                send_activation_email(new_user, token)

                messages.info(request,"Successfully Registered. Please check your email for activation.")
            
            # Redirect to login page after successful registration
                return redirect('home:login')
            else:
                messages.info(request, "Passwords do not match")
                return redirect('home:register')
            
        else:

            form = CustomUserCreationForm()
            print("test1")
            messages.info(request, "username or email id existing")
            return redirect('home:register')


    else:
        form = CustomUserCreationForm()
        print("test1")
    return render(request,"register.html",{'form': form})
    

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        tokens = force_str(urlsafe_base64_decode(token))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and token_is_valid(user, tokens):
        print(user)
        print(user.is_active)
        if user.is_active == True:
            messages.info(request, 'Your account is already activated')
            return redirect('accounts:login')
        user.is_active = True
        user.save()
        messages.info(request, 'Your account has been activated successfully')
        return redirect('home:acc_setup',email=user.email)
    else:
        messages.info(request, 'Activation link is invalid')
        return redirect('home:login')

def send_activation_email(user, token):
    uname=user.username
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    ttoken = urlsafe_base64_encode(force_bytes(token))
    print("enc tocken : ",ttoken)
    # activation_link = f"http://127.0.0.1:8000/accounts/activate/{uid}/{ttoken}"  # Replace with your activation URL
    # message = f"Please click the following link to activate your account: {activation_link}"
    # send_mail(
    #     'Activate Your Account',
    #     message,
    #     settings.DEFAULT_FROM_EMAIL,
    #     [user.email],
    #     fail_silently=False,
    # )

    email_subject="Activate Acoount"
    message=render_to_string('mails/account_activation_link.html',{
            
            'uname':uname,
            'uid':uid,
            'ttoken':ttoken,
            
        })
    print("mail attemptting")
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    email_message = EmailMessage(email_subject,message,email_from,recipient_list)
    print(email_message)
    email_message.content_subtype = "html"
    email_message.send()


def login(request):
#    if request.method == 'POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         print(username)
#         print(password)
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             print(user)
            
#             if user.is_staff or user.is_superuser:
#                 login(user)
#             return redirect('home:profile')
    return render(request,"login.html")




   
def profile(request):
    user = request.user
    context = {}

    try:
        # Attempt to get the SocialAccount associated with the user
        social_account = SocialAccount.objects.get(user=user)

        # If the SocialAccount exists, retrieve the associated EmailAddress
        email_address = EmailAddress.objects.get(email=user.email)

        # Populate the context with user, email_address, and social_account
        context = {
            'user': user,
            'email_address': email_address,
            'social_account': social_account
        }
        print("1")
    except SocialAccount.DoesNotExist:
        # If the SocialAccount does not exist, retrieve the User object only
        user = User.objects.get(email=user.email)
        context = {
            'user': user
        }
        print("2")
    except EmailAddress.DoesNotExist:
        print("3")
        # Handle the case where EmailAddress does not exist for the user
        pass
    
    return render(request,"dashboard/profile.html",context)

def setting(request):
    return render(request,"dashboard/settings.html")

def notification(request):
    return render(request,"dashboard/notifications.html")

def bookandhistory(request):
    return render(request,"dashboard/bookandhistory.html")

def invoice(request):
    return render(request,"dashboard/invoice.html")

def account_setup(request):
    return render(request,"dashboard/account_setup.html")




# settings page tabs

def profile_edit(request):
    return render(request,"dashboard/settings/profile_edit.html")

def pass_update(request):
    return render(request,"dashboard/settings/password_update.html")

def acc_update(request):
    return render(request,"dashboard/settings/account_update.html")

def support(request):
    return render(request,"dashboard/settings/support_center.html")

def demo(request):
    return render(request,"dashboard/settings.html")



# account setup
def acc_setup(request):
    countries = Country.objects.all()
    email = request.GET.get('email', None)

    # states = Region.objects.filter(country=india)
    # cities = City.objects.filter(region__in=states)
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name','')
        last_name = request.POST.get('last_name','')
        username = request.POST.get('username','')
        account_type = request.POST.get('account_type','')
        address = request.POST.get('address','')
        postcode = request.POST.get('postcode','')
        country = request.POST.get('country','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        profile_dp = request.FILES.get('profile_dp')

        # print(first_name)
        # print(last_name)
        # print(username)
        # print("ACC",account_type)
        # print(address)
        # print(postcode)
        # print(country)
        # print(city)
        # print(state)
        # print(profile_dp)



        return redirect('home:acc_setup')

        

    return render(request,"acc_setup_base_form.html",{'countries': countries,'email':email })

def get_states(request):
    country_id = request.GET.get('country_id')
    states = Region.objects.filter(country_id=country_id)
    state_list = [{'id': state.id, 'name': state.name} for state in states]
    return JsonResponse({'states': state_list})

# ajax code for citys based on states
def get_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(region_id=state_id)
    city_list = [{'id': city.id, 'name': city.name} for city in cities]
    return JsonResponse({'cities': city_list})

