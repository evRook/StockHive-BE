from rest_framework import serializers
from .models import Company, History

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