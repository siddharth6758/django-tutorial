from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    country = models.CharField(max_length=100)
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    person_id = models.ForeignKey(Person,on_delete=models.CASCADE)