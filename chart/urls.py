from django.urls import path
from . import views

urlpatterns = [
	path('line/', views.ChartView.as_view(), name='demo'),
	path('lineUpdate/', views.ChartUpdateView.as_view(), name='demo'),
	path('index/', views.IndexView.as_view(), name='demo'),
]

