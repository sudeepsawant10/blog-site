from django.db import models

# Create your models here.
#Category Modle
#models.Model => attributes to create columns of Model
class Category(models.Model):
    #column name
    #accepted if no value
    name = models.CharField(max_length = 255, null=True, blank = True)

    def __str__(self):
        return self.name
    