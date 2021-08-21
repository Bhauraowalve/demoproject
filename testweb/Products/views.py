from django.shortcuts import render ,HttpResponseRedirect , redirect
from .forms import NewUserForm 
from Products.forms import *
from Products.models import Product 
from django.contrib.auth.decorators import login_required 



# Create your views here. 
def index_view(request): 
    return render(request,'Products/index.html') 

@login_required
def add_product_view(request): 
    form=ProductForm() 
    if request.method=='POST': 
        form=ProductForm(request.POST) 
        if form.is_valid(): 
            form.save() 
        return index_view(request) 
    return render(request,'Products/addproduct.html',{'form':form}) 

def list_product_view(request): 
    product_list=Product.objects.all().order_by('-price') 
    return render(request,'Products/listproduct.html',{'product_list':product_list}) 

def signup_view(request): 
    form=SignUpForm() 
    if request.method=='POST': 
        form=SignUpForm(request.POST) 
        user=form.save() 
        user.set_password(user.password) 
        user.save() 
        return HttpResponseRedirect('/login/') 
    return render(request,'Products/signup.html',{'form':form}) 

def logout_view(request): 
    auth.logout(request)
    return render(request,'Products/logout.html')


from django.contrib.auth.forms import  AuthenticationForm 
from django.contrib.auth.models import auth
from django.contrib import messages
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/addproduct')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,template_name = "Products/login.html",context={"form":form})