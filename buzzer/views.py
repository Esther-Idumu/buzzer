from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile, Buzz
from .forms import BuzzForm
from django.http import HttpResponse

def home(request):
        if request.user.is_authenticated:
            form = BuzzForm(request.POST or None)
            if request.method == 'POST':
                if form.is_valid():
                    buzz = form.save(commit=False)
                    buzz.user = request.user
                    buzz.save()
                    messages.success(request, ("Your buzz has been posted"))
                    return redirect('home')

            buzzes = Buzz.objects.all().order_by("-created_at")
            return render(request, 'home.html', {"buzzes":buzzes, "form":form,},)
        else:
            buzzes = Buzz.objects.all().order_by("-created_at")
            return render(request, 'home.html', {"buzzes":buzzes,}, )

#Render signup page
def signup(request):
    if request.method == 'POST':
        #print("POST data:", request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(password, confirm_password)

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                print('Username already exists')
                messages.error(request, 'Username already taken.')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
        else:
            print('passwords did not match')
            return render(request, 'signup.html')
    return render(request, 'signup.html')

# Render login page
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)

        if user:
            login(request, user)  
            messages.success(request,' Login successful')
            return redirect('home')
        else:
            return render(request, 'login.html')
            messages.error(request, 'You must log in first')
    return render(request, 'login.html')

# Logout view 
def logout_user(request):
    logout(request) 
    #messages.success(request, 'You have been logged out.')
    return redirect('login')

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {'profiles': profiles})
    else:
        messages.success(request, ("You must be logged in to view this page"))
        return redirect(request, 'login')

def profile_view(request, pk):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user_id=pk)
            buzzes = Buzz.objects.filter(user_id=pk)
            # Post form logic
            if request.method == "POST":
                # Get current user
                current_user_profile = request.user.profile
                # Get form data
                action = request.POST['follow']
                # Decide to follow or unfollow
                if action == "unfollow":
                    current_user_profile.follows.remove(profile)
                else:
                    current_user_profile.follows.add(profile)
                # Save the profile
                current_user_profile.save()

            return render(request, 'profile.html', {'profile': profile, 'buzzes':buzzes})
        except Profile.DoesNotExist:
            messages.error(request, "Profile not found")
            return redirect('profile_list')
    else:
        messages.success(request, ("You must be logged in to view this page"))
        return render(request, 'home.html')


