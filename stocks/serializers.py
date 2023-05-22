from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from .models import History, CompanyInfo

User = get_user_model()

class HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = History
        fields = (
            'id',
            'symbol',
            'validRanges',
            'Open', 
            'Close', 
            'High', 
            'Low', 
            'Volume',
        )

class CompanyInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = (
            'id',
            'symbol', 
            'shortName',
            'longName',
            'address1',
            'city', 
            'state', 
            'country',
            'phone',
            'website',
            'sector',
            'longBuisnessSummary', 
            'auditRisk',
            'boardRisk',
            'compensationRisk',
            'shareHolderRightsRisk',
            'overallRisk',
            'open',
            'dayLow',
            'dayHigh',
            'currentPrice',
            'beta',
            'volume',
            'averageVolume',
            'marketCap',
            'targetMeanPrice',
            'dividendRate',
            'dividendYield',
            'forwardPE',
            'regularMarketPreviousClose',
            'regularMarketOpen',
            'regularMarketDayLow',
            'regularMarketDayHigh',
            'marketCap',
            'fiftyTwoWeekHigh',
            'fiftyTwoWeekLow',
            'currency',
            'recommendationMean',
            'recommendationKey',
        )

class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first',
            'last',
            'email',
            'password',
        )