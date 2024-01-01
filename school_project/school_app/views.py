from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import  messages
from .forms import  Register
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        messages.info(request, "You have Succesfully Login. Click Register to Register students")


    return render(request,'login.html')

def register(request):
    # Implement registration logic
    if request.method == 'POST':
        username = request.POST['username']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        email =  request.POST['email']
        address = request.POST['address']
        purpose = request.POST['Purpose']
        dept = request.POST.get('dept','')
        course = request.POST.get('course','')
        materials = request.POST.get('materials_provided','')
        messages.info(request,"Order Placed")

        user = User.objects.create_user(username=username, dob=dob, age=age,gender=gender,email=email,address=address,
                                        purpose=purpose,dept=dept,course=course,materials=materials)
        user.save()

    return render(request, 'register.html')