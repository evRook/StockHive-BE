from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class History(models.Model):
    ticker = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='history')
    date = models.DateField()
    open = models.IntegerField()
    close = models.IntegerField()
    dividends = models.IntegerField()
    splits = models.IntegerField()

    def __str__(self):
        return self.ticker