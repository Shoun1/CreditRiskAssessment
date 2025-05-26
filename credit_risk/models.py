from django.db import models

# Create your models here.
class Borrower(models.Model):
    grade = models.CharField(max_length=1)
    defaulter = models.CharField(max_length=1)
    class Meta:
        db_table = 'Borrower'

class Plots(models.Model):
    name = models.CharField(max_length=100)
    plot = models.ImageField(upload_to='plots/')
    class Meta:
        db_table = 'Plots'