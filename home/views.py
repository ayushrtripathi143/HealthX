from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from home.models import Patient_Appointment,add_hospital_data,appointment_rest_data,medical_remainder,medical_rest_data
from multi_form_view import MultiFormView
from .forms import medical_remainder_form,medical_rest_data_form

import openai,os


# Create your views here.
def index(request):
    return render(request,'index.html')

def chatbot(request):
   
    return render(request,'chatbot.html')

def about(request):
    return HttpResponse("this is about")

def temp_nav(request):
    return render(request,'temp_nav.html')

def teamsignup(request):
    return render(request,'teampageup.html')

def maps(request):
    return render(request,'map.html')

def button(request):
    return render(request,'button.html')

def second_page(request):
    return render(request,'second_page.html')

def consulting_landing(request):
    return render(request,'consulting_landing.html')

def services(request):
    return HttpResponse("this is services")

def staff_login(request):
    if request.method=="POST":
        name=request.POST.get('email')
        password=request.POST.get('password')
        print(name,password)
        if name=="sanidhy" and password=="1234":
            return redirect('doctors_dashboard')
    return render(request,'staff_login.html')



def admin_login(request):
    if request.method=="POST":
        name=request.POST.get("mail")
        password=request.POST.get("password")
        if name=="sanidhy" and password=="1234":
            return redirect('admin_dashboard')
    return render(request,'admin_login.html')


def add_hospital(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mail=request.POST.get('mail')
        phone=request.POST.get('Contact_Number')
        capaity=request.POST.get('capaity')
        beds=request.POST.get('beds')
        oxygen=request.POST.get('oxygen')
        date=request.POST.get('date')
        city=request.POST.get('city')
        dept=request.POST.get('department')
        address=request.POST.get('address')
        print(name,mail,phone,capaity,oxygen,beds,date,city,dept,address)
        ins = add_hospital_data(name=name,mail=mail,phone=phone,capaity=capaity,beds=beds,oxygen=oxygen,date=date,city=city,dept=dept,address=address)
        ins.save()
        print("Save")
    return render(request,'Add_hospital.html')

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')


def medicine_remainder(request):
   medical_remainder1=medical_remainder()
   medical_rest_data1=medical_rest_data()
   print("o")
   if request.method=="POST":
    print("QWERTYUI")
    if 'medical_remainder' in request.POST:
        print("1")
        medical_remainder1=medical_remainder(request.POST)
        if medical_remainder1.is_valid():
            print("yes")
            name=request.POST.get('name')
            email=request.POST.get('email')
            print(name,email)
    elif 'medical_rest_data' in request.POST:
        print("2")
        medical_rest_data1=medical_rest_data(request.POST)
        if medical_rest_data1.is_valid():
            email=request.POST.get('email')
            medicine_name=request.POST.get('medicine_name')
            does=request.POST.get('does')
            no_of_days=request.POST.get('days')
            remarks=request.POST.get('message')
            print(email,medicine_name,does,no_of_days,remarks)
   return render(request,'medicne_remainder.html')


def view_appointment(request):
    query = request.GET.get('q')
    if query:
        print(query)
    if query:
        rest_data=appointment_rest_data.objects.filter(hospital=query)
    else:
        rest_data=appointment_rest_data.objects.filter(hospital=query)
    patient_data=Patient_Appointment.objects.all()
    context={'patient_data':patient_data,'rest_data':rest_data}
    return render(request,'view_appoitments.html',context)


def ThankYou(request):
    return render(request,'Thankyou.html')


def aboutus(request):
    return render(request,'aboutus.html')

def appointment(request):
    # context ={'sucess': False, 'name':'Yes'}
    if request.method=="POST":
        name=request.POST.get('name')
        mail=request.POST.get('email')
        contact_no=request.POST.get('Contact_Number')
        DOB=request.POST.get('DOB')
        gender=request.POST.get('gender')
        city=request.POST.get('city')
        dept=request.POST.get('department')
        address=request.POST.get('address')
        print(name,mail,contact_no,DOB,gender,city,dept,address)
        appointment=Patient_Appointment(name=name,mail=mail,phone=contact_no,dob=DOB,gender=gender,city=city,dept=dept,address=address)
        appointment.save()
        print("data written to db")
        return redirect('confirm_appoint')
    return render(request,'appoint.html')

def confirm_appoint(request):
    allTasks=add_hospital_data.objects.all()
    newTasks=Patient_Appointment.objects.last()
    
    if request.method=="POST":
        hospital=request.POST.get('hospital')
        desc=request.POST.get('desc')
        mail=newTasks.mail
        dept=newTasks.dept
        print(hospital,date,desc,mail)
        confirm_data=appointment_rest_data(hospital=hospital,desc=desc,mail=mail,dept=dept)
        confirm_data.save()
        print("data written to db")
        return render(request,'Thankyou.html')
    # print(allTasks)
    # for item in allTasks:
    #     print(item.name)
    context={'tasks':allTasks,'patient_info':newTasks}
    return render(request,'confirm_appoint.html',context)


def new(request):
    if request.method=="POST":
        username=request.POST.get('Username')
        pass1=request.POST.get('pass')
        # print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('second_page')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request,'new.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        # print(uname,email,pass1,pass2)
        if pass1!=pass2:
            return HttpResponse("Your PassWord are not same")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('new')
    return render(request,'signup.html')


def date(request):
    print("NO")
    last_user=appointment_rest_data.objects.latest('mail')
    if request.method=='POST':
        date=request.POST.get('date')
        last_user.date=date
        last_user.save()
        print("uo0")
    return render(request,'datetime.html')



def doctors_dashboard(request):
    return render(request,'doctors_dashboard.html')


@login_required(login_url='new')
def second_main(request):
    return render(request,'second_main.html')



def launch_project2(request):
    return redirect('http://localhost:8001/store')