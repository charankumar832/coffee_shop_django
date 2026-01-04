from django.urls import path
from .views import home,products,contact, loginuser, signupuser,logoutuser, findproduct

urlpatterns = [
    path('',home,name='home'),
    path('products/',products,name='products'),
    path('contact/',contact, name='contact'),
    path('login/', loginuser, name='loginuser'),
    path('signup/', signupuser, name='signupuser'),
    path('logout/', logoutuser, name='logoutuser'),
    path('findproduct/', findproduct, name='findproduct'),
]
