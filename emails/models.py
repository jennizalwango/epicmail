from django.db import models

class User(models.Model):
  created_on = models.DateTimeField(auto_now_add=True)
  first_name = models.CharField('first_name', max_length=50)
  last_name = models.CharField('last_name', max_length=50)
  email = models.CharField('email', max_length=100)
  password = models.CharField('password', max_length=100)
    
  def __str__(self):
    return "{}-{}-{}-{}-{}".format(self.created_on, self.first_name, self.last_name, self.email, self.password)
# Create your models here.
