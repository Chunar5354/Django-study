from django.urls import path
from . import views

urlpatterns = [
	path('currentchart/', views.CurrentChart.as_view(), name='chart'),
	path('voltagechart/', views.VoltageChart.as_view(), name='chart'),
	path('temperaturechart/', views.TemperatureChart.as_view(), name='chart'),
	path('lineUpdate/', views.ChartUpdateView.as_view(), name='chart'),
	path('index/', views.IndexView.as_view(), name='chart'),
	path('current/', views.CurrentView.as_view(), name='chart'),
	path('voltage/', views.VoltageView.as_view(), name='chart'),
	path('temperature/', views.TemperatureView.as_view(), name='chart'),
]

