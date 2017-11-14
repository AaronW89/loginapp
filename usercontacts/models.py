from django.db import models

# Create your models here.
class Contact(models.Model):
    Owner = models.ForeignKey('auth.User')
    FirstName = models.CharField(max_length=30,blank=False)
    LastName = models.CharField(max_length=30,blank=False)
    Email = models.EmailField(max_length=50, blank=True)

    def __str__(self):
        return self.LastName + ", " + self.FirstName
        