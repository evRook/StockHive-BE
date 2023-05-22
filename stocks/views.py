from django.shortcuts import render, redirect
from django.template import loader


from .models import History, CompanyInfo, UserAcct
from .serializers import HistorySerializer, CompanyInfoSerializer, UserCreateSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
import yfinance as yf
import datetime
import requests

# Create your views here.

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
    

class TickerList(APIView):
    serializer_class = CompanyInfoSerializer

    def get(self, request):
        ticker_list = ['aapl', 'msft', 'tsla', 'f', 'meta', 'jnj', 'wmt', 'jpm',  'intc', 'googl', 'aapl', 'pypl', 'amzn', 'amd', 'nvda', 'gme', 'ko']
        context_list = []
        for ticker in ticker_list:
            ticker_obj = yf.Ticker(ticker)
            ticker_info = ticker_obj.info
            context = [{
                'symbol': ticker_info['symbol'],
                'shortName': ticker_info['shortName'],
                'currentPrice': ticker_info['currentPrice'],
                'regularMarketPreviousClose': ticker_info['regularMarketPreviousClose'],
            }]
            context_list.append(context)
        
        return Response(context_list)



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
            'currentPrice': info['currentPrice'],
            'beta': info['beta'],
            'volume': info['volume'],
            'averageVolume': info['averageVolume'],
            'marketCap': info['marketCap'],
            'targetMeanPrice': info['targetMeanPrice'],
            'forwardPE': info['forwardPE'],
            'regularMarketPreviousClose': info['regularMarketPreviousClose'],
            'regularMarketOpen': info['regularMarketOpen'],
            'regularMarketDayLow': info['regularMarketDayLow'],
            'regularMarketDayHigh': info['regularMarketDayHigh'],
            'marketCap': info['marketCap'],
            'fiftyTwoWeekHigh': info['fiftyTwoWeekHigh'],
            'fiftyTwoWeekLow': info['fiftyTwoWeekLow'],
            'currency': info['currency'],
            'recommendationMean': info['recommendationMean'],
            'recommendationKey': info['recommendationKey'],
        }]

        return Response(context)


