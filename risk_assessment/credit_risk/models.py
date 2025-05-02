from django.db import models

# Create your models here.
class Borrower(models.Model):
    grade = models.CharField(max_length=1)
    defaulter = models.CharField(max_length=1)
    class Meta:
        db_table = 'Borrower'