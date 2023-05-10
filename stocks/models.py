from django.db import models

# Create your models here.
class Company(models.Model):
    Symbol = models.CharField(null=True, max_length=10)
    Name = models.CharField()

    def __str__(self):
        return self.Symbol

class History(models.Model):
    Company_id = models.ForeignKey(Company, null=True, on_delete=models.CASCADE, related_name='history')
    Open = models.IntegerField()
    Close = models.IntegerField()
    High = models.IntegerField()
    Low = models.IntegerField()

    def __str__(self):
        return self.Company_id