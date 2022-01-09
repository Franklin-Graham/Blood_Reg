from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages,auth
from donor_app.models import donor_data
# Create your views here.
def Index(request):
    return render(request,'home.html')

def Register(request):
    if request.method == "POST":
        username = request.POST['user']
        # email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User name already exist")
                return redirect('sign_app:register')
            if request.POST["user"] == '':
                messages.info(request,"Please fill Credentials")
                return redirect('sign_app:register')
            if request.POST["password"] == "":
                messages.info(request, "Please fill Credentials")
                return redirect('sign_app:register')
            if request.POST["cpassword"] == "":
                messages.info(request, "Please fill Credentials")
                return redirect('sign_app:register')

            # elif User.objects.filter(email=email).exists():
            #     messages.info(request,"Email already exits")
            #     return redirect('sign_app:register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('sign_app:login')

        else:
            messages.info(request,"password not matching")
            return redirect('sign_app:register')
        return redirect('/')

    return render(request,'registration.html')

def Login(request):
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('donor_app:donate')
        else:
            messages.info(request,'please enter correct credentials')
            return redirect('sign_app:login')
    return render(request,'login.html')

def Logout(request):
    auth.logout(request)
    return redirect('/')

#validate login
def Validate(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['dpassword']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('sign_app:confirm')
        else:
            messages.info(request, 'please enter correct credentials')
            return redirect('sign_app:validate')
    return render(request, 'validate.html')

def Confirm(request):
    if request.method == "POST":
        blood = request.POST['group']
        blood_group = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]

        if request.POST['group'] == "select":
            messages.info(request, "Please Select Your Blood Group*")
            return redirect('sign_app:confirm')

        if request.POST['group'] in blood_group:
            messages.info(request,f"you are donating {blood} blood group. your credentials submitted successfully...")
            return redirect('sign_app:confirm')



    return render(request, 'confirm.html')
