from django.db import models
from django.urls import reverse

class employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=20)
    eadd=models.CharField(max_length=30)
    esal=models.FloatField()
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.ename

    def get_absolute_url(self):
        return reverse('employee_list')

