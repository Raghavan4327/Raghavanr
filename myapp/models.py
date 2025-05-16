from django.db import models


# Model for MyForm
# models.py
from django.db import models

class MyUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Email should be unique
    password = models.CharField(max_length=255)  # Store the password (hashed)

    def __str__(self):
        return self.name



# Model for UserData
class mydata(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    password = models.CharField(max_length=255)


    def __str__(self):
        return self.name

# Model for AdminData
class vkdata(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    dob = models.DateField()
    company_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)
    address = models.TextField()


    def __str__(self):
        return self.name


