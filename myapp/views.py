from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

from django.shortcuts import render

from .forms import userdata
from .forms import admindata
from django.shortcuts import render


def login(request):
    return render(request, 'login.html')




from django.shortcuts import render, redirect
from .forms import MyForm
from .models import MyUser
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from .forms import userdata
from .models import mydata

def base(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # Use cleaned data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check if email already exists in the database
            if MyUser.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already registered.')
                return render(request, 'login.html', {'form': form})

            # Hash the password before saving
            hashed_password = make_password(password)

            # Save to the database
            user = MyUser(name=name, email=email, password=hashed_password)
            user.save()

            # After saving, redirect to the base view (success redirect)
            return redirect('base')  # Ensure you're redirecting to a valid URL
        else:
            # If form is invalid, re-render the page with form errors
            return render(request, 'login.html', {'form': form})

    # Handle GET request
    else:
        form = MyForm()  # Create a new empty form instance
        return render(request, 'login.html', {'form': form})





from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import userdata  # Replace with your actual form
from .models import mydata   # Replace with your actual model
from .models import vkdata
from .forms import admindata

def register(request):
    if request.method == "POST":
        data = userdata(request.POST)
        if data.is_valid():
            name  = data.cleaned_data['name ']
            email = data.cleaned_data['email']
            Contact = data.cleaned_data['Contact']
            password = data.cleaned_data['password']


            if mydata.objects.filter(email=email).exists():
                data.add_error('email', 'This email is already registered.')
                return render(request, 'reg.html', {'data': data})

            hashed_password = make_password(password)
            user = mydata(name=name , email=email, contact=Contact, password=hashed_password)
            user.save()

            return redirect('base')
        else:
            return render(request, 'reg.html', {'data': data})
    else:
        data = userdata()  # Initialize empty form for GET
        return render(request, 'reg.html', {'data': data})

      
def clientdata(request):
    if request.method == "POST":
        data = admindata(request.POST)
        if data.is_valid():
            name = data.cleaned_data['name']
            email = data.cleaned_data['email']
            dob = data.cleaned_data['dob']
            company_name = data.cleaned_data['company_name']
            contact = data.cleaned_data['contact']
            address = data.cleaned_data['address']

            if vkdata.objects.filter(email=email).exists():
                data.add_error('email', 'This email is already registered.')
                return render(request, 'contact.html', {'data': data})
            
            user = vkdata(name=name, email=email, dob=dob,
                           company_name=company_name, contact=contact,address=address)
            user.save()

            return redirect('base')

        else:
              return render(request, 'contact.html', {'data': data}) 
    else:
        data=admindata()
        return render(request, 'contact.html',{'data': data})
     


