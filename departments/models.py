from django.db import models
from django.db.models import signals


class Department(models.Model):
    name = models.CharField(max_length=50)
    empoyees_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name + ' Department'


class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_of_birth = models.DateField('Date of birth')
    solary = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name + ' from ' + str(self.department)




