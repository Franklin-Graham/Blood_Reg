from django.db import models


# Create your models here.
class donor_data(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    phn_no = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=150)
    address = models.TextField()
    district = models.CharField(max_length=250)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return 'Blood Group'+ " " + str(self.blood_group)+ " " + "is" + " " + "available"
