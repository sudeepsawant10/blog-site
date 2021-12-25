# to redirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

# importing UserCreate class from forms.py
from .forms import UserCreate

from django.views import View

# for success message
from django.contrib import messages

#for login and logout purpose import these
from django.contrib.auth import authenticate, login, logout

# Create your views here.

""" Function Based Views """


# def index(request):
#     return HttpResponse("<h1>Welcome to index page</h1>")


# def Home(request):
#     return render(request, 'BlogApp/home.html')


# # def Home2(request):
# #     return render(request, 'BlogApp/home2.html')


# def Contact(request):
#     # return HttpResponse("<h1>Welcome to Contact page</h1>")
#     return render(request, 'BlogApp/contact.html')


# def Login(request):
#     # return HttpResponse("<h1>Welcome to Contact page</h1>")
#     return render(request, 'BlogApp/login.html')


# def Register(request):
#     return render(request, 'BlogApp/register.html')


# def About(request):
#     return render(request, 'BlogApp/about.html')


""" Class Based Views"""


class Home(View):
    def get(self, request):
        return render(request, 'BlogApp/home.html')
    # def post() used for forms


class Login(View):
    #when user visit login/ url render this page
    def get(self, request):
        return render(request, 'BlogApp/login.html')

    #when user submit the login credentials
    def post(self, request):

        #function for checking the filled attributes in login page with the data base values
        #username and password will store the values filled by user
        #the authenticate function will compare these values with database user model username and password
        #if valid user will get True other wise none
        user = authenticate(
            request, username=request.POST['inputUsername'], password=request.POST['inputPassword'])
            # request, username=request.POST['inputEmail'], password=request.POST['inputPassword'])
        # email = request.POST['inputEmail']
        if user:
            login(request, user)
            print('******************', user)

            #if user.is_staff means it y are admin so show this response staff=>database access superuser=>can change data
            #domain will be same but userid will be different for ecah user (primary key usr=id to access we use user.id i.e. object.id)
            if user.is_staff:
                
                return redirect('userhome', id=user.id)
                # return HttpResponse('<h1>U are Admin</h1>')
            
            #if user is normal then redirect to userhome url with user.id this url will call some views active=>allow to login not banned
            elif user.is_active:
                #id = user.id it will take id of above authenticated username
                return redirect('userhome', id=user.id)
                # return HttpResponse('<h1>U are Admin</h1>'))
            #show login page
            else:
                return redirect('login')
         #if user is not authenticated show again login page
        else:
            return redirect('login')


class Register(View):
    # def get(self, request):
    #     return render(request, 'BlogApp/login.html')

    # To pass form restrictions or structure to register.html if user comes to register/ url
    def get(self, request):
        # calling normal url page
        # object of UserCreate class
        user_create = UserCreate()

        # dictionary that store User form Structure object data in user_create key
        context = {'user_create': user_create}

        # passing
        return render(request, 'BlogApp/register.html', context)

    # when user submit the registeration form
    def post(self, request):
        # request.POST means submit the data in this Model and also store the data in object to check data is valid or not according to UserCreate class restrictions

        #take all data filled by user in user_create
        user_create = UserCreate(request.POST)

        # data is filled according to requirements and restirctions then it is valid
        if user_create.is_valid():
            # ready to save temporarily save
            user_create = user_create.save(commit=False)
            # permenent save
            user_create.save()
            # display this message after saving data into user database
            messages.success(request, 'Account created successfully.')
            # go to login url
            return redirect('login')
        else:
            # messages.errors(request, user_create_form.errors)
            # if not valid again take the structure and restriction of form and pass to regitser.html
            context = {'user_create': user_create}

            # add into form
            return render(request, 'BlogApp/register.html', context)


class About(View):
    def get(self, request):
        return render(request, 'BlogApp/about.html')


class Blogs(View):
    def get(self, request):
        return render(request, 'BlogApp/blogs.html')


def Logout(request):
    #to logout use this inbuilt function
    logout(request)
    print("logout succussfull")
    #redirect to home
    return redirect('home')
