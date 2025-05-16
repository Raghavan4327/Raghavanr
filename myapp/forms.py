from django import forms

# forms.py
from django import forms
from .models import MyUser

# forms.py
from django import forms
from .models import MyUser
from .models import mydata
from .models import vkdata

class MyForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['name', 'email', 'password']  # These fields correspond to the MyUser model

    name = forms.CharField(
        max_length=100,
        label="Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name-input', 'placeholder': 'Enter your name'})
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email-input', 'placeholder': 'Enter your email'})
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password-input', 'placeholder': 'Enter your password'})
    )

    
class userdata(forms.Form):
    class Meta:
        model = mydata
        fields = ['name', 'email','Contact', 'password'] 
    
    name = forms.CharField(
        max_length=20,
        label="Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name-input'
        ,'placeholder': 'Enter your name'})
    )
    email = forms.CharField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'
        , 'id': 'email-input', 'placeholder': 'Enter your email'})
    )
    Contact = forms.CharField(
        max_length=15,
        label="Contact",
        widget=forms.TextInput(attrs={'class': 'form-control',
         'id': 'contact-input', 'placeholder': 'Enter your contact'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 
        'id': 'password-input', 'placeholder': 'Enter your password'})
    )

class admindata(forms.Form):
    class Meta:
        model = vkdata
        fields = ['Name', 'Email','dob', 'company_name','contact','address'] 
    name  = forms.CharField(
        max_length=20,
        label="Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name-input',
        'placeholder': 'Enter your name'})
    )
    email  = forms.CharField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 
        'id': 'email-input','placeholder': 'Enter your email'})
    )
   
    dob = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'date-field',
            'id': 'dob-input',
          
        })
    )

    company_name = forms.CharField(
        max_length=30,
        label="Company Name",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'company-input',
            'placeholder': 'Enter your company name'
        })
    )

    contact = forms.CharField(
        max_length=15,
        label="Contact",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'contact-input',
            'placeholder': 'Enter your contact number'
        })
    )

    address = forms.CharField(
        label="Address",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'address-input',
            'rows': 3,
            'placeholder': 'Enter your address',
        }))


