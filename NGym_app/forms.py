from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Calories1,Employee,Position



class LoginForm(forms.Form):
    username=forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    First_Name = forms.CharField()
    Last_Name = forms.CharField()
    username=forms.CharField()
    email=forms.EmailField()
    password_first = forms.CharField(widget=forms.PasswordInput())
    password_again = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data=self.cleaned_data
        password_one=self.cleaned_data.get('password_first')
        password_two = self.cleaned_data.get('password_again')
        if ((password_one) != (password_two)):
            raise forms.ValidationError("Password doesn't match")
        return cleaned_data

    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username unavailable")
        return username

    def clean_email(self):
        email_address=self.cleaned_data.get('email')
        qs = User.objects.filter(email=email_address)
        if qs.exists():
            raise forms.ValidationError("email already registered")
        return email_address





class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=('fullname','mobile','emp_code','position')
        labels={
            'fullname':"Full Name",
            "emp_code":"Emp Code"
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="Select"
        self.fields["mobile"].required=False

class Calories(forms.ModelForm):
    class Meta:
        model=Calories1
        fields=('Name',"Age","Weight","Height","Choices")
        labels={
            'Choices':"Physical Activity",
        }

    def __init__(self,*args,**kwargs):
        super(Calories,self).__init__(*args,**kwargs)
        self.fields['Choices'].empty_label="Select Activity"