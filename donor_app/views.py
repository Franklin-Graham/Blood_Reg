from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import *
# Create your views here.
def index(request):
    return render(request, 'home.html')

def donate(request):
    if request.method == "POST":
        donor_name = request.POST['user']
        age = request.POST['age']
        phone = request.POST['phone']
        blood_group = request.POST['blood_group']
        address = request.POST['text']
        district = request.POST['district']
        gender = request.POST['gender']
        donor_user = donor_data.objects.create(name=donor_name, age=age, phn_no=phone,
                                            blood_group=blood_group, address=address,
                                            district=district, gender=gender)
        if donor_data is None:
            messages.info(request,"Please fill the credentials")
            return redirect('donor_app:donate')
        else:
            return redirect('sign_app:validate')
        # if donor_user is not None:
        #     return redirect('sign_app:login')
        # else:
        #     messages.info(request, "Please fill the credentials")
    return render(request, 'donate.html')
