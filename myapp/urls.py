from django.urls import path
from . import views


from django.urls import path


urlpatterns = [
    path('base/', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('clientdata/', views.clientdata, name='clientdata' ),
    ]

