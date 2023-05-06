from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    history = serializers.HyperlinkedRelatedField(
        view_name='history',
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