from django.shortcuts import render, redirect
from .models import Product,Contact_Query
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def home(request):
    products_info=Product.objects.all()[:6]
    return render(request, 'coffee_app/home.html', {'products_info':products_info})

@login_required(login_url='loginuser')
def products(request):
    products_info=Product.objects.all()
    paginator=Paginator(products_info,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    return render(request, 'coffee_app/products.html',{'page_obj':page_obj})

def contact(request):
    if request.method=='GET':
        return render(request, 'coffee_app/contact.html')
    
    elif request.method=='POST':
        name=request.POST.get('name',None)
        email=request.POST.get('email', None)
        msg=request.POST.get('msg',None)

        if not name or not email or not msg:
            return render (request, 'coffee_app/contact.html',{'error':'Name, Email and Msg are mandatory Fields'})
        
        if Contact_Query.objects.filter(email=email).exists():
            return render(request, 'coffee_app/contact.html',{'error':'Email already exists. Try with new email.'})
            
        
        new_data=Contact_Query.objects.create(name=name, email=email, msg=msg)
        new_data.save()

        return render(request, 'coffee_app/contact.html',{'success':'Successfully Sent'})
    
def loginuser(request):

    if request.method=='GET':
        return render(request, 'coffee_app/loginuser.html', {'form':AuthenticationForm()})
    
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if not user:
            return render(request, 'coffee_app/loginuser.html',{'form':AuthenticationForm(),'error':'Inavlid Credentials'})
        else:
            login(request, user=user)
            return redirect('home')


def signupuser(request):
    if request.method=='GET':
        return render(request, 'coffee_app/signupuser.html',{'form':UserCreationForm()})
    
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password!=password2:
            return render(request, 'coffee_app/signupuser.html',{'form':UserCreationForm(), 'error':'Password Mismatch'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'coffee_app/signupuser.html', {'form':UserCreationForm(),'error':'Username already exists. Try with another'})
        
        user=User.objects.create_user(username=username, password=password)
        user.save()
        
        login(request, user=user)
        return redirect('home')


def logoutuser(request):
    logout(request)
    return redirect('home')

def findproduct(request):
    if request.method=='GET':
        product_search=request.GET.get('product_search','').strip()
    
    elif request.method=='POST':
        product_search=request.POST.get('product_search','').strip()

    my_data=Product.objects.filter(Q(product_name__icontains=product_search)|Q(product_category__icontains=product_search)|Q(product_description__icontains=product_search))
    
    paginator=Paginator(my_data,3)
    page_number=request.GET.get('page',1)
    page_obj=paginator.get_page(page_number)
    return render (request, 'coffee_app/products.html', {'page_obj':page_obj, 'search_item':product_search})




        

