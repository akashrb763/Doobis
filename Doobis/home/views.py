from django.shortcuts import render,redirect
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages,auth
import json

# Create your views here.

def home(request):
    return render(request,"index.html")


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

def register(request):
    return render(request,"register.html")
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

