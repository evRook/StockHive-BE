from django.urls import path
from . import views

urlpatterns = [
    path('docs/company/', views.CompanyList.as_view(), name='company_list'),
    path('docs/company/<int:pk>', views.CompanyDetail.as_view(), name='company_detail' ),
    path('docs/history/', views.HistoryList.as_view(), name='history_list'),
    path('docs/history/<int:pk>', views.HistoryDetail.as_view(), name='history_detail'),
    path('get/company/<int:pk>', views.search_data, name='history_create'),
    path('company/', views.GetCompany.as_view(), name='companys_list')
]