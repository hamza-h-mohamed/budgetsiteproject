from django.db import models
from django.utils import timezone

class Saving(models.Model):

    amount = models.IntegerField()

class Checking(models.Model):

    amount = models.IntegerField()

class Spending(models.Model):
    
    maxSpendAmount = models.IntegerField()
    bills = models.IntegerField()
    food_drink = models.IntegerField()
    gas = models.IntegerField()
    personal_expense = models.IntegerField()

class Report(models.Model):

    CHOICES_TYPES = [
        ('Bills','Bills'),
        ('Food_Drinks','Food_Drinks'),
        ('Gas','Gas'),
        ('Personal_Expense','Personal_Expense'),
    ]
    name = models.CharField(
        max_length=50,
        choices=CHOICES_TYPES, 
        default='Personal_Expense'
    )
    date_pushed = models.DateTimeField(default=timezone.now)
    maxAmount = models.IntegerField()

    def amount(self):
        spent = list(Report.objects.aggregate(Sum('maxAmount')).values())[0] or 0 # the or 0 is required in case the query is an empty query set.
        return spent