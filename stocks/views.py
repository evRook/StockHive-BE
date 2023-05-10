from django.shortcuts import render, redirect
from django.template import loader


from .models import Company, History
from .serializers import CompanySerializer, HistorySerializer
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

# def search_data(request, pk):
#     spec = Company.objects.get(id=pk)
#     spec_symbol = spec.Symbol
#     start = "2023-04-05"
#     finish = "2023-04-06" 
#     stock = yf.Ticker(spec_symbol)
#     data = stock.history(start = start, end = finish)
#     index = list(data.index.strftime('%Y-%m-%d %H'))
#     close = data.Close.values.tolist()
#     open = data.Open.values.tolist()
#     high = data.High.values.tolist()
#     low = data.Low.values.tolist()
#     return JsonResponse( {pk :{'index': index, 'close': close, 'open': open,'high': high, 'low': low}}, status = 200)

class GetCompany(APIView):
    serializer_class = CompanySerializer

    def get(self, request):
        data = [ {"Symbol": data.Symbol, "Name": data.Name} 
        for data in Company.objects.all()]
        return Response(data)


# def GetCompanyInfo(request):
    
