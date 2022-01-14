from django.db import models

# Create your models here.
class User(models.Model):
    
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)
    age = models.IntegerField()
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)
    zip = models.IntegerField()
    email = models.EmailField()
    web = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.firstName