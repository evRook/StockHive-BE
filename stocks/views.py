from django.shortcuts import render, redirect
from django.template import loader


from .models import Company, History, CompanyInfo
from .serializers import CompanySerializer, HistorySerializer, CompanyInfoSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
import yfinance as yf
import datetime

# Create your views here.

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class HistoryList(generics.ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class HistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class CompanyInfoList(generics.ListCreateAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer


class GetCompanyInfo(APIView):
    serializer_class = CompanyInfoSerializer

    def get(self, request):

        context = [ {
            'symbol': data.symbol, 
            'shortName': data.shortName,
            'longName': data.longName,
            'address1': data.address1,
            'city': data.city, 
            'state': data.state, 
            'country': data.country,
            'phone': data.phone,
            'website': data.website,
            'sector': data.sector,
            'logBuisnessSummary': data.longBuisnessSummary, 
            'overallRisk': data.overallRisk,
            'open': data.open,
            'dayLow': data.dayLow,
            'dayHigh': data.dayHigh,
            'regularMarketPreviousClose': data.regularMarketPreviousClose,
            'regularMarketOpen': data.regularMarketOpen,
            'regularMarketDayLow': data.regularMarketDayLow,
            'regularMarketDayHigh': data.regularMarketDayHigh,
            'marketCap': data.marketCap,
            'fiftyTwoWeekHigh': data.fiftyTwoWeekHigh,
            'fiftyTwoWeekLow': data.fiftyTwoWeekLow,
            'currency': data.currency,
        }
        for data in CompanyInfo.objects.all()]
        return Response(context)


class GetCompany(APIView):
    serializer_class = CompanySerializer

    def get(self, request):
        context = [ {"Symbol": data.Symbol, "Name": data.Name} 
        for data in Company.objects.all()]
        return Response(context)

    
