#lbrary to create models
from django.db import models

#importing catefory model to use it as foreign key constriant in Blog Modle
from BlogApp.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    #title added by user for blog
    #Compulsory data required
    title = models.CharField(max_length = 255, blank=False, null = False)
    #Optional
    description = models.CharField(max_length = 255, blank = True, null = True)
    #Date time Field
    post_date = models.DateTimeField()
    #optional
    delet_date = models.DateTimeField(null=True)
    #Category Table(Model) Foreign key
    #on_delete=models.SET_NULL)=>if delete we will set foreign key as null
    #set_cascade=>foreing key  rows will delete if primary key deleted 
    category_id =  models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    #user Foring key by using User inbuilt table
    #To specify who add the blog
    owner = models.ForeignKey(User, null=True,on_delete = models.SET_NULL)
    # likes = models.ManyToManyField(User,blank=True, related_name='likes')

    # #if this not present admin panel will show u as Blog object
    def __str__(self):
        return self.title + ' ' + str(self.owner)

#django uses sqli database
#To reflect table on sqlui
"""
go to command
makemigrations
migrate

Tables will not be visible in admin panel until u registered it
"""