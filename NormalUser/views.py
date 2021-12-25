from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

#for logged in action when user visit mannually in logged in functionality url
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

#importing form
from . forms import BlogCreateForm
# Use user in this model
from django.contrib.auth.models import User

from . models import Blog
from  BlogApp.models import Category
from . forms import CreateCategory
# Create your views here.


# def NormalUser(request):
#     return HttpResponse("<h1>This is Normal User Page</h1>")


# Create your views here.
#for logged in user view
class RegUser(LoginRequiredMixin, View):
    #we are taking id from views.py of BlogApp to urls.py of NomralUser app to views.py of Normal user
    #kwargs means we are taking multiple arguments from urls.py of NormalUser
    def get(self, request, **kwargs):
        #Explicitly taking only 'id' from karguments and assining it to key id
        # context = {'id': kwargs['id'],'username': kwargs['username']}
        context = {'id': kwargs['id']}
        #passing user id to this will call automatically userhome
        return render(request, 'NormalUser/home.html', context)


#To display and to create the blog
class NewBlog(LoginRequiredMixin, View):
    #Display form with structure
    def get(self, request, **kwargs):
        new_blog = BlogCreateForm()
        #user have logged in so we pass his id and this id will help to add his user data into db
        #id will be used in nav.html becoz we have already extended it and it will be use to add data into db
        #Category.objects.all()=> django query similar to select *from catregory
        context = {'new_blog':new_blog, 'id':kwargs['id'], 'catogerys':Category.objects.all() }
        return render(request, 'NormalUser/new.html', context)
    
    #Create Blog and add data to db(handle submit)
    def post(self, request, **kwargs):
        #Taking fields value into object
        new_blog = BlogCreateForm(request.POST)
        #checking fields are valid or not
        if new_blog.is_valid():
            new_blog = new_blog.save(commit = False)
            #who add the blog taking using django query and saving it into  Blog(Model)
            new_blog.owner = User.objects.get(id=kwargs['id'])
            new_blog.save()
            #after successfully adding blog
            #redirecting to userhome and passing id bocoz id takes url
            return redirect('my_blog', id=kwargs['id'])
        else:
            #if not valid do this
            new_blog = BlogCreateForm(request.POST)
            context={'new_blog':new_blog, 'id':kwargs['id']}
            return render(request, 'NormalUser/new.html', context)

class MyBlog(LoginRequiredMixin, View):
    #Display blog to user
    def get(self, request, **kwargs):
        #create object of Blog Model to display all the blogs
        my_blog = Blog()
        #fetch all rows
        my_blog = Blog.objects.filter(owner=kwargs['id'])
        #take rows and pass to template
        context={'my_blog':my_blog, 'id':kwargs['id']}
        #render
        return render(request, 'NormalUser/my_blogs.html', context)


class AllBlogs(LoginRequiredMixin, View):
    #display all the blogs of all the users
    def get(self, request, **kwargs):
        #create object of Blog Model to display all the blogs
        my_blog = Blog()
        #fetch all rows
        my_blog = Blog.objects.all()
        #take rows and pass to template
        context={'my_blog':my_blog, 'id':kwargs['id']}
        #render
        return render(request, 'NormalUser/all_blogs.html', context)


class NewCategory(View, LoginRequiredMixin):
    def get(self, request, **kwargs):
        new_category = CreateCategory()
        context = {'new_category': new_category, 'id':kwargs['id']}
        return render(request, "NormalUser/category.html", context)

    def post(self, request, **kwargs):
        #we store all the form field(name) required for category model in this object.
        new_category = CreateCategory(request.POST)
        if new_category.is_valid():
            #saving filed in Category table
            new_category = new_category.save(commit=False)
            new_category.save()
            return redirect('all_categories', kwargs['id'])
        else:
            context = {'new_category': new_category, 'id':kwargs['id']}
            return render(request, "NormalUser/category.html", context)
            

class AllCategory(View, LoginRequiredMixin):
    def get(self, request, **kwargs):
        All_Category= Category.objects.all()
        context={'All_Category': All_Category, 'id': kwargs['id']}
        return render(request, "NormalUser/allcat.html", context)

class EditCategory(View, LoginRequiredMixin):
    def get(self, request, **kwargs):
        category = Category.objects.get(id=kwargs['cid'])
        #Taking Existing Category and displaying it into form filed(category.html where we create the category) to for edit.
        #form filed name
        edit_category = CreateCategory(instance=category)
        context = {
            'new_category': edit_category,
            'id': kwargs['id']
        }
        return render(request, "NormalUser/category.html", context)

    def post(self, request, **kwargs):
        category = Category.objects.get(id=kwargs['cid'])
        #Taking updating value from filed and saving into object and form and updaing into Category table
        edit_category = CreateCategory(request.POST, instance = category)
        if edit_category.is_valid():
            edit_category = edit_category.save(commit=False)
            edit_category.save()
            return redirect('all_categories', id=kwargs['id'])
        else:
            edit_category = CreateCategory(instance=category)
            context = {
                'new_category': edit_category,
                'id': kwargs['id']
            }
            return render(request, "NormalUser/category.html", context)
 
class DeleteCategory(View, LoginRequiredMixin):
    def get(self, request, **kwargs):
        Category.objects.get(id=kwargs['cid']).delete()
        all_categories=Category.objects.all()
        context={
            'All_Category':all_categories,
            'id':kwargs['id']
        }
        return render(request, "NormalUser/allcat.html", context)