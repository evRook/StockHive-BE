from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompanyList.as_view(), name='company_list'),
    path('history/', views.HistoryList.as_view(), name='history_list'),
]