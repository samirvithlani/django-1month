from statistics import mode

from django.db import models

# Create your models here.
#class baesd models..
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    isActive = models.BooleanField(default=True)
    address = models.TextField()
    joining_date = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = 'student'
        
    def __str__(self):
        return self.name    

CHOICE = [
    ("work from home","work from home"),
    ("work from office","work from office")
]
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    salary = models.FloatField()
    contactNo = models.CharField(max_length=100)
    workchoice = models.CharField(max_length=100,choices=CHOICE)
    isMarried = models.BooleanField(null=True)
    
    class Meta:
        db_table = "employee"
        
    def __str__(self):
        return self.name   

catChoice = [
    ("Eletronices","eletoronics"),
    ("Fashion","fashion"),
    ("Books","books"),
]
class Category(models.Model):            
    name = models.CharField(max_length=100,choices=catChoice)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField() 
    qty = models.IntegerField()    
    
    def __str__(self):
        return self.name
    

cchoice = [
    ("java",("fs,es,google")),
    ("php",("yt,clg")),
    ("python",("uni,ech")),
]

class Tut(models.Model):
    name=models.CharField(max_length=100)
    choice = models.CharField(max_length=100,choices=cchoice)    