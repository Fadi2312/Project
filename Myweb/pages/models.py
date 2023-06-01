from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class Etud_Cours(models.Model):
    Dep = models.CharField(max_length=70)
    Modul = models.CharField(max_length=70)
    description = models.TextField()
    title = models.CharField(max_length=70)
    link= models.CharField(max_length=100)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title
    
    
class Etud_Questions(models.Model):
    Depp = models.CharField(max_length=70)
    Modull = models.CharField(max_length=70)
    descriptionn = models.TextField()
    titlee = models.CharField(max_length=70)
    image= models.ImageField(upload_to=None, height_field=None, width_field=None,null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.titlee
    
    
class Comment(models.Model):
    post = models.ForeignKey(Etud_Questions,on_delete=models.CASCADE,related_name="comments")
    name = models.CharField(max_length=255)
    content = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
            return self.name
        
class Admin_Ann(models.Model):
    Dep_Ann = models.CharField(max_length=200)
    Description_Ann = models.CharField(max_length=200)
    title_Ann = models.CharField(max_length=100)
    Link_Ann = models.CharField(max_length=500)
    added_Ann = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 
    def __str__(self):
            return self.title_Ann
    
    
    
    
    
      
