import imp
from tabnanny import check
from unicodedata import name
from wsgiref.util import request_uri
from django.shortcuts import render,redirect
from .forms import SignUpForm, LoginForm
from schoolhome.models import studentregistrations,teacherregistrations,checkstudent
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def register(request):

    msg = None

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        

        if form.is_valid():
            username = form.cleaned_data.get('username')
            registeras = form.cleaned_data.get('registeras')
            checking = checkstudent(username=username,check_type = registeras )
            checking.save()
        

            user = form.save()
            
            return redirect('stulog')
            
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form,'msg': msg})


def stulog(request):
 
    form = LoginForm(request.POST or None)
    msg = None
    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
           
            password = form.cleaned_data.get('password')
          
            user = authenticate(username=username, password=password)
            request.session['username'] = username
            login(request, user)
            checkingst = checkstudent.objects.get(username= username)
            if(checkingst.check_type  == 'student'):
                return redirect('studentregistration')
            else:
                return redirect('teacherregistration')


            

            
        
        else:
            msg = 'error validating form'
    return render(request, 'stulog.html', {'form': form, 'msg': msg})


def studentregistration(request):
    usernames =  request.user.get_username()
    
    if not request.user.is_authenticated:
        return redirect('/')
    checkexiststudent = studentregistrations.objects.all()

    for checkingstudent in checkexiststudent:
        if(usernames == checkingstudent.username):
            return redirect('studentprofile')

    if request.method == "POST":
        
        nam = request.POST.get('nam')
        class1 = request.POST.get('cls')
        div = request.POST.get('div')
        roll = request.POST.get('roll')
        contact = request.POST.get('contact')
        stinfo =studentregistrations(username =usernames ,name = nam,class1= class1,div=div,roll=roll,contact=contact)
        stinfo.save()
        return redirect('studentprofile')



    

    return render(request,'studentregistration.html')
def teacherregistration(request):
    usernames =  request.user.get_username()
    
    if not request.user.is_authenticated:
        return redirect('/')
    checkexiststudent = teacherregistrations.objects.all()

    for checkingstudent in checkexiststudent:
        if(usernames == checkingstudent.username):
            return redirect('studentprofile')

    if request.method == "POST":
        
        nam = request.POST.get('nam')
        class1 = request.POST.get('cls')
        div = request.POST.get('div')
        
        contact = request.POST.get('contact')
        stinfo =teacherregistrations(username =usernames ,name = nam,class1= class1,div=div,contact=contact)
        stinfo.save()
        return redirect('studentprofile')



    

    return render(request,'teacherregistration.html')



def studentprofile(request):
    if not request.user.is_authenticated:
        return redirect('/')
    usernames =  request.user.get_username()
    sinfo = studentregistrations.objects.get(username = usernames)
    name = sinfo.name
    clas = sinfo.class1
    div =sinfo.div
    roll =sinfo.roll
    contact = sinfo.contact

    context = {
        'username' :usernames,
       'name' :name,
       'classs' :clas,
       'div' : div,
       'roll':roll,
       'contact':contact
    }


    return render(request,'studentprofile.html',context=context)


def logoutstudent(request):
    logout(request)
    return redirect('stulog')
    