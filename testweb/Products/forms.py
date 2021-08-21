from django import forms 
from Products.models import Product 
from User.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class  ProductForm(forms.ModelForm): 
#fields with validations 
    class Meta: 
        model=Product 
        fields='__all__'

class LoginForm(forms.Form):
    name =forms.CharField()

class SignUpForm(forms.ModelForm): 
    class Meta: 
        model=User 
        fields=['first_name','last_name','email','password','username'] 

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user