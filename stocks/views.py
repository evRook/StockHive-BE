from django.shortcuts import render, redirect
from django.template import loader


from .models import Company, History, CompanyInfo, UserAcct
from .serializers import CompanySerializer, HistorySerializer, CompanyInfoSerializer, UserCreateSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
import yfinance as yf
import datetime
import requests

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

class UserList(generics.ListAPIView):
    queryset = UserAcct.objects.all()
    serializer_class = UserCreateSerializer

class GetHistory(APIView):
    serializer_class = HistorySerializer

    def get(self, request, pk, pk_alt):
        ticker = yf.Ticker(pk)
        meta = ticker.history_metadata
        history = ticker.history(period=pk_alt)
        history_list = history.values.tolist()
        context = [{
            'symbol': meta['symbol'],
            'validRanges': meta['validRanges'],
            'Open': [],
            'Close': [],
            'High': [],
            'Low': [],
            'Volume': []
        }]
        for hist in history_list:
            context[0]['Open'].append(
                hist[0], 
            )
            context[0]['Close'].append(
                hist[1], 
            )
            context[0]['High'].append(
                hist[2], 
            )
            context[0]['Low'].append(
                hist[3], 
            )
            context[0]['Volume'].append(
                hist[4], 
            )

        return Response(context)

class GetCompanyInfo(APIView):
    serializer_class = CompanyInfoSerializer

    def get(self, request, pk):
        ticker = yf.Ticker(pk)
        info = ticker.info
        context = [{
            'symbol': info['symbol'],
            'shortName': info['shortName'],
            'longName': info['longName'],
            'address1': info['address1'],
            'city': info['city'], 
            'state': info['state'], 
            'country': info['country'],
            'phone': info['phone'],
            'website': info['website'],
            'sector': info['sector'],
            'longBusinessSummary': info['longBusinessSummary'],
            'auditRisk': info['auditRisk'],
            'boardRisk': info['boardRisk'],
            'compensationRisk': info['compensationRisk'],
            'shareHolderRightsRisk': info['shareHolderRightsRisk'],
            'overallRisk': info['overallRisk'],
            'open': info['open'],
            'dayLow': info['dayLow'],
            'dayHigh': info['dayHigh'],
            'regularMarketPreviousClose': info['regularMarketPreviousClose'],
            'regularMarketOpen': info['regularMarketOpen'],
            'regularMarketDayLow': info['regularMarketDayLow'],
            'regularMarketDayHigh': info['regularMarketDayHigh'],
            'marketCap': info['marketCap'],
            'fiftyTwoWeekHigh': info['fiftyTwoWeekHigh'],
            'fiftyTwoWeekLow': info['fiftyTwoWeekLow'],
            'currency': info['currency'],
        }]

        return Response(context)


class GetCompany(APIView):
    serializer_class = CompanySerializer

    def get(self, request):
        context = [ {"Symbol": data.Symbol, "Name": data.Name} 
        for data in Company.objects.all()]
        return Response(context)


