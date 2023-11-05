from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm,UserRegistrationForm
from faculty.models import flogin
# Create your views here.

def profile(request):
    return HttpResponse('<h1> This is faculty profile page </h1>')
def bi (request):
    return HttpResponse('<h1> This is bookissued page </h1>')
def faculty_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request,'faculty/FHome.html')  # Redirect to faculty dashboard
            else:
                # Handle invalid login credentials
                return render(request, 'faculty/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'faculty/login.html', {'form': form})



#
# from django.template import loader
# import mysql.connector
#
# from django.shortcuts import render
# # from .forms import InputForm
# # Create your views here.
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="#Traveller07",
#   database="LMS",
# )
#
# def myStudent(request):
#     userid = (request.GET.get('userid')) #Fetch value from the HTML Page
#     passw = (request.GET.get('password'))
#     myCursor = mydb.cursor()
#     # if userid == "0":
#     #     myCursor.execute("SELECT * FROM userMaster")
#     # else:
#     #     myCursor.execute("SELECT * FROM userMaster where studid = " + str(userid))
#
#     myresult = myCursor.fetchall()
#
#     rc = myCursor.rowcount
#     #Sample to Insert, update and delete query
#     myCursor.execute("INSERT INTO userMaster VALUES("+str(userid)+","+str(passw)+")")
#     mydb.commit()
#
#     res= "<Table border=1>"
#     for x in myresult:
#         res = res +"<tr><td>"+ str(x[0]) + " </td><td>" +  str(x[1]) + "</td></tr>"
#
#     return HttpResponse("Total Records > " + str(rc) + "<BR> Available Data :"+ res )

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request,'faculty/FHome.html')  # Replace 'home' with the name of your homepage URL
    else:
        form = UserRegistrationForm()

    return render(request, 'faculty/registration.html', {'form': form})

