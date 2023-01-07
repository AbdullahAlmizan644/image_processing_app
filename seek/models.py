from django.db import models

# Create your models here.


class Person(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    division=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    address=models.CharField(max_length=1000)
    present_address=models.CharField(max_length=1000)
    about=models.CharField(max_length=1000)
    GENDER = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    gender = models.CharField(max_length=1, choices=GENDER, null=True)
    nid_number=models.IntegerField()
    person_image=models.ImageField(upload_to="static/seek/images/")
    nid_image=models.ImageField(upload_to="static/seek/images/")
    fingerprint_image=models.ImageField(upload_to="static/seek/images/")
    date=models.DateField()

    def __str__(self):
        return f"id:{self.id} name:{self.first_name} {self.last_name}"

