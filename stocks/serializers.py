from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from .models import Company, History, CompanyInfo

User = get_user_model()

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    history = serializers.HyperlinkedRelatedField(
        view_name='history_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Company
        fields = (
            'id',
            'Symbol',
            'Name',
            'history',
        )

class HistorySerializer(serializers.HyperlinkedModelSerializer):
    Company_id = serializers.PrimaryKeyRelatedField(
        queryset = Company.objects.all()
    )

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
    Company_id = serializers.PrimaryKeyRelatedField(
        queryset = Company.objects.all()
    )

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
            'overallRisk',
            'open',
            'dayLow',
            'dayHigh',
            'regularMarketPreviousClose',
            'regularMarketOpen',
            'regularMarketDayLow',
            'regularMarketDayHigh',
            'marketCap',
            'fiftyTwoWeekHigh',
            'fiftyTwoWeekLow',
            'currency',
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