from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_detail' ),
    path('user/favorties', views.FavoritesList.as_view(), name='user_favorites'),
    path('user/favorties/<str:pk>', views.FavoritesDetail.as_view(), name='user_detail'),

    # yf api calls
    path('company/<str:pk>', views.GetCompanyInfo.as_view(), name='companyinfo_list'),
    path('ticker', views.TickerList.as_view(), name='ticker_list'),
    path('history/<str:pk>/<str:pk_alt>', views.GetHistory.as_view(), name='companyinfo_list'),
    
    # User
    path('auth/', include('djoser.urls'), name='auth'),
    path('auth/', include('djoser.urls.jwt'), name='auth_jwt'),

]

urlpatterns += [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html'))
]