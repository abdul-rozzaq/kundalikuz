from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout as lgt, login as lgn
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from project.models import Content, Day

from datetime import datetime

@login_required(login_url='login')
def home_page(request):
    if request.method == 'POST':
        
        day = request.POST.get('day')
        
        if day:
            queryset = Day.objects.filter(date=day, user=request.user)
            
            if not queryset.exists():
                day = Day.objects.create(date=day, user=request.user)
                
                return redirect('day', pk=day.pk)
        else:
            return redirect(request.META.get('HTTP_REFERER'))
    
    days = Day.objects.filter(user=request.user).order_by('date')
    
    return render(request, 'index.html', {'days': days})

@login_required(login_url='login')
def day_page(request, pk):    
    day = Day.objects.get(pk=pk)
    
    if day.user != request.user:
        return redirect('home')
    
    if request.method == 'POST':
        body =  request.POST.get('body')
        
        if body:
            content = Content.objects.create(day=day, text=body)
            
            return redirect('day', pk=day.pk)
    
    contents = Content.objects.filter(day=day, )
        
    return render(request, 'day.html', {'day': day, 'contents': contents})


@login_required(login_url='login')
def delete(request, pk):
    
    content = Content.objects.get(pk=pk)
    day = content.day
    
    if day.user != request.user:
        return redirect('home')
        
    content.delete()
    
    return redirect('day', pk=day.pk)
    
    
@login_required(login_url='login')
def delete_content(request, pk):
    content = Content.objects.get(pk=pk)
    day = content.day
    
    
    if day.user != request.user:
        return redirect('home')
            
    return render(request, 'delete_content.html', {'content': content})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            lgn(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'login.html')
    
def logout(request):
    lgt(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(username, password1, password2)
        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1)
            lgn(request, user)
            
            return redirect('home')
    
    return render(request,'register.html')