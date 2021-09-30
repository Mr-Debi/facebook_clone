from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from.models import Profile,Post
# Create your views here.
def Login(request):             #dont save in small login cuz(django have allready login files)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        if not request.user.is_anonymous:           #anonymous == unNonne
            return redirect(home)
        else:
            return render(request,'index.html')
    
# def home(request):
#     return HttpResponse(""" 
#     <center>
#         <h1>This is Home Page. </h1>
#     </center>
#     """)

def home(request):
    if request.user.is_authenticated:
        user = request.user
        nmae = user.first_name +' '+user.last_name
        pro = Profile.objects.get(user=user)
        pos = Post.objects.filter(user=user)
        context = {'name':nmae,
        'pro':pro,
        'pos':pos}      #these are dictionary
    return render(request,'home.html',context)

def profile(request):
    if request.user.is_authenticated:
        pro = Profile.objects.get(user=request.user)
        return render(request,'profile.html',{'pro':pro})
    else:
        return redirect('login')

# ------------------------
def contact(request):
    if request.user.is_authenticated:
        pro = Profile.objects.get(user=request.user)
        return render(request,'contact.html',{'pro':pro})
    else:
        return redirect('login')

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create(username=username)
            user.set_password(password2)
            user.save()
            return redirect('login')
        else:
            return redirect('login')
    else:
        return redirect('login')
            
def create_post(request):
    if request.method=='POST':
        content = request.POST['content']
        p = Post.objects.create(user=request.user,post =content)
        p.save()
        return redirect('home')

def update_profile(request):
    if request.method=='POST':
        status= request.POST['status']
        loc = request.POST['location']
        # pic = request.POST['fileToUplode']
        
        p = Profile.objects.get(user=request.user)
        p.status = status
        p.location = loc
        # p.image = pic
        p.save()
        return redirect('profile')

# def uplode_pic(request):
#     if request.method=='POST':
