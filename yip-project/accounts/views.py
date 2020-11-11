from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import logout,login
from django.contrib.auth.models import User
from django.http import JsonResponse

from .models import extendedteaminfo

# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is None: return render(request,'accounts/login.html',{'error':"Username or Password is incorrect"})
        else :
            auth.login(request, user)
            return redirect('home')
    else: return render(request,'accounts/login.html')

def logout(request):
    # logout the user and redirect to homepage
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['teamname'])
                return render(request,'accounts/signup.html',{'error':"This Team name is already taken"})

            except User.DoesNotExist:
                # s1gender = request.POST.get('s1gender', "X");
                # s2gender = request.POST.get('s2gender', "X");
                # s3gender = request.POST.get('s3gender', "X");

                user = User.objects.create_user(request.POST['teamname'],password=request.POST['password1'])
                newteamdata = extendedteaminfo(                
                school=request.POST['school'],
                team_name=request.POST['teamnamecap'],
                ps=request.POST['ps'],
                teacher_name=request.POST['teachername'],
                teacher_email=request.POST['teacheremail'],
                teacher_phone_num=request.POST['teacherphone'],
                num_of_students=request.POST['group1'],
                user=user,

                s1_name=request.POST['s1name'],
                s1_email=request.POST['s1email'],
                s1_phone_num=request.POST['s1phone'],
                s1_class=request.POST['s1class'],
                s1_dob=request.POST['s1dob'],
                s1_gender=request.POST['s1gender'],

                s2_name=request.POST['s2name'],
                s2_email=request.POST['s2email'],
                s2_phone_num=request.POST['s2phone'],
                s2_class=request.POST['s2class'],
                s2_dob=request.POST['s2dob'],
                s2_gender=request.POST['s2gender'],

                s3_name=request.POST['s3name'],
                s3_email=request.POST['s3email'],
                s3_phone_num=request.POST['s3phone'],
                s3_class=request.POST['s3class'],
                s3_dob=request.POST['s3dob'],
                s3_gender = request.POST.get('s3gender', "")
                )

                newteamdata.save()
                auth.login(request,user)
                return dashboard(request)
        else: return render(request,'accounts/signup.html',{'error':"Enter same password in both fields."})

    else:
        return render(request,'accounts/signup.html')
def teamname_check(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "GET":
        try:
            user = User.objects.get(username = request.GET.get("teamname", None))
            return JsonResponse({"valid":False}, status = 200)
        except User.DoesNotExist: return JsonResponse({"valid":True}, status = 200)

def show(request):

    all_objects= extendedteaminfo.objects.all()
    
    context= {'all_objects': all_objects}
        
    return render(request, 'yip/show.html', context)
         
def dashboard(request): return render(request,'accounts/dashboard.html')