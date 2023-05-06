from django.db import models

# Create your models here.
class Company(models.Model):
    Symbol = models.CharField(null=True, max_length=10)
    Name = models.CharField()

    def __str__(self):
        return self.Symbol

class History(models.Model):
    ticker = models.ForeignKey(Company, null=True, on_delete=models.CASCADE, related_name='history')
    date = models.DateField()
    open = models.IntegerField()
    close = models.IntegerField()
    dividends = models.IntegerField()
    splits = models.IntegerField()

    def __str__(self):
        return self.ticker