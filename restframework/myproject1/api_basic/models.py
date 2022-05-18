from django.db import models

# Create your models here.

class Employeemodel(models.Model):
    empname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    salary = models.IntegerField()
    
    class Meta:
        db_table = "employee"

