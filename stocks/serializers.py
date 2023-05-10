from rest_framework import serializers
from .models import Company, History, CompanyInfo

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
            'Company_id',
            'Open', 
            'Close', 
            'High', 
            'Low', 
        )

class CompanyInfoSerializer(serializers.HyperlinkedModelSerializer):
    Company_id = serializers.PrimaryKeyRelatedField(
        queryset = Company.objects.all()
    )

    class Meta:
        model = CompanyInfo
        fields = (
            'id',
            'Company_id',
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
            'logBuisnessSummary', 
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