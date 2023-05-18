from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class Company(models.Model):
    Symbol = models.CharField(null=True, max_length=10)
    Name = models.CharField()

    def __str__(self):
        return self.Symbol

class History(models.Model):
    symbol = models.CharField(null=True)
    validRanges = ArrayField(models.CharField(null=True, blank=True), blank=True,)
    Open = ArrayField(models.IntegerField(null=True, blank=True), blank=True,)
    Close = ArrayField(models.IntegerField(null=True, blank=True), blank=True,)
    High = ArrayField(models.IntegerField(null=True, blank=True), blank=True,)
    Low = ArrayField(models.IntegerField(null=True, blank=True), blank=True,)
    Volume = ArrayField(models.IntegerField(null=True, blank=True), blank=True,)
    
    def __str__(self):
        return self.symbol
    
class CompanyInfo(models.Model):
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
    longBuisnessSummary = models.TextField()
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
    
class UserAcctManager(BaseUserManager):
    def create_user(self, first, last, email, user_name=None,  password=None):
        email_norm = self.normalize_email(email)
        user = self.model(first=first, last=last, email=email_norm)
        user.set_password(password)
        user.save()

        return user


class UserAcct(AbstractBaseUser, PermissionsMixin):
    first = models.CharField()
    last = models.CharField()
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first', 'last']

    objects = UserAcctManager()

    def __str__(self):
        return self.email