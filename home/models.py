from django.db import models
from django.utils import timezone
from django.db.models import Sum

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
    

class Summary(models.Model):
    summary = models.BooleanField(null=True)
    summaryAmount = models.IntegerField(null=True)

    def amount(self):
        if self.summary == True:
            self.summaryAmount = list(Report.objects.aggregate(Sum('maxAmount')).values())[0] or 0 # the or 0 is required in case the query is an empty query set.
        else:
            s = Summary.objects.all()
            s.delete()
        return self.summaryAmount
