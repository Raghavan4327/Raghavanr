# admin.py
from django.contrib import admin
from .models import MyUser, mydata,vkdata  # Correct the import statement

# Register your models here
admin.site.register(MyUser)  # Register the MyUser model
admin.site.register(mydata)  # Register userdata model
admin.site.register(vkdata)  # Register AdminData model (if you have it)


# Register your models here.
