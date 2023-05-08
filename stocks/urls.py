from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompanyList.as_view(), name='company_list'),
    path('company/<int:pk>', views.CompanyDetail.as_view(), name='company_detail' ),
    path('history/', views.HistoryList.as_view(), name='history_list'),
]