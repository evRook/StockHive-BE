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
    
class CompanyInfo(models.Model):
    Company_id = models.ForeignKey(Company, null=True, on_delete=models.CASCADE, related_name='company_info')
    symbol = models.CharField()
    shortName = models.CharField()
    longName = models.CharField()
    address1 = models.CharField()
    city = models.CharField()
    state = models.CharField()
    country = models.CharField()
    phone = models.CharField()
    website = models.CharField()
    sector = models.CharField()
    logBuisnessSummary = models.CharField()
    overallRisk = models.IntegerField()
    open = models.IntegerField()
    dayLow = models.IntegerField()
    dayHigh = models.IntegerField()
    regularMarketPreviousClose = models.IntegerField()
    regularMarketOpen = models.IntegerField()
    regularMarketDayLow = models.IntegerField()
    regularMarketDayHigh = models.IntegerField()
    marketCap = models.IntegerField()
    fiftyTwoWeekHigh = models.IntegerField()
    fiftyTwoWeekLow = models.IntegerField()
    currency = models.CharField()

    def __str__(self):
        return self.symbol
