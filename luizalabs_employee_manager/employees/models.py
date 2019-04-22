from django.db import models

# Create your models here.


class Employee(models.Model):
    """
    Model Employee
    """
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    department = models.CharField('Department', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['name']
