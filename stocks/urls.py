from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('docs/company/', views.CompanyList.as_view(), name='company_list'),
    path('docs/companyinfo/', views.CompanyInfoList.as_view(), name='company_list'),
    path('docs/company/<int:pk>', views.CompanyDetail.as_view(), name='company_detail' ),
    path('docs/users', views.UserList.as_view(), name='user_detail' ),
    path('docs/history/', views.HistoryList.as_view(), name='history_list'),
    path('docs/history/<int:pk>', views.HistoryDetail.as_view(), name='history_detail'),
    
    # yf api calls
    path('company/', views.GetCompany.as_view(), name='companys_list'),
    path('company/<str:pk>', views.GetCompanyInfo.as_view(), name='companyinfo_list'),
    path('history/<str:pk>', views.GetHistory.as_view(), name='companyinfo_list'),
    
    # User
    path('auth/', include('djoser.urls'), name='auth'),
    path('auth/', include('djoser.urls.jwt'), name='auth_jwt'),

]

urlpatterns += [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html'))
]