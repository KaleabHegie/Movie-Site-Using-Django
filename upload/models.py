from django.db import models

# Create your models here.


    
class Pricing(models.Model):
    type = models.CharField(max_length=50)
    montlyFee = models.CharField(max_length=10)
    vedioQuality = models.CharField(max_length=10)
    resulution = models.CharField(max_length=10)
    maxScreen = models.IntegerField()  

    def __str__(self) -> str:
        return self.type

class Blog(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='')   


    def __str__(self) -> str:
        return self.title
    
class Contact(models.Model):
    adress = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.adress   

class Movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.DateField()
    resulution = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)
    rating = models.FloatField()
    discription = models.TextField()
    genere = models.CharField(max_length=40 )
    category = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='')
    

    def __str__(self) -> str:
        return self.name       
