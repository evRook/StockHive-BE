from django.urls import path
from . import views

urlpatterns = [
    path('docs/company/', views.CompanyList.as_view(), name='company_list'),
    path('docs/companyinfo/', views.CompanyInfoList.as_view(), name='company_list'),
    path('docs/company/<int:pk>', views.CompanyDetail.as_view(), name='company_detail' ),
    path('docs/history/', views.HistoryList.as_view(), name='history_list'),
    path('docs/history/<int:pk>', views.HistoryDetail.as_view(), name='history_detail'),

    path('company/', views.GetCompany.as_view(), name='companys_list'),
    path('company/<str:pk>', views.GetCompanyInfo.as_view(), name='companyinfo_list')
]