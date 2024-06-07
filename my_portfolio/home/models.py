from django.db import models

# Create your models here.
class About(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    dob_me = models.DateField(null=True)
    about = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to='images/')

