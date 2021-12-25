from django.forms import ModelForm
from .models import Blog
from BlogApp.models import Category

#Blog form structure for Blog Modle
#To read multiple fields of model at same time to perform some operation in future.
class BlogCreateForm(ModelForm):
    class Meta:
        #table name
        #This will take all the columns of Model Blog
        model = Blog
        #attributes category_id will be name of catigory django will automatically detect this
        #Only this fiels will be used in new.html form to edit and adding purpose
        fields = ['title', 'description', 'post_date', 'category_id']
        
class CreateCategory(ModelForm):
    class Meta:
        #table name
        #This will take all the columns of Model Blog
        model = Category
        #attributes category_id will be name of catigory django will automatically detect this
        #Only this fiels will be used in new.html form to edit and adding purpose
        fields = ['name']
