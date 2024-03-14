from django.shortcuts import render

# Create your views here.


def doobiz_franch_acc_setup(request):
    if request.method == "POST":
        name=request.POST.get('name','')
        phone=request.POST.get('phone','')
        address=request.POST.get('address','')
        pin=request.POST.get('pin','')
        proof=request.POST.get('proof','')


        print(name)
        print(phone)
        print(address)
        print(pin)
        print(proof)
       
    return render(request,"doobiz_franchise/account_setup.html")

def req_validation(request):
    
       
    return render(request,"doobiz_franchise/req_validation.html")