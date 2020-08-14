import json
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Line
from pyecharts import options as opts

from django.shortcuts import render
from django.db.models import Max

from . import models


class Chart():
	def __init__(self, Module):
		self.Module = Module
		self.index = 1000  # Set a big init value so it will run get_value_from_db() at beginning
		self.data_list = []

	def get_value_from_db(self):
		last_time = self.Module.objects.last().create_time
		values = self.Module.objects.filter(create_time=last_time)
		self.data_list = [i.value for i in values]

	def get_data(self, length):
		if self.index >= length:
			self.get_value_from_db()
			self.index = 0
		else:
			self.index += length // 5
		return self.data_list[self.index : self.index + length//5]
		

def response_as_json(data):
	json_str = json.dumps(data)
	response = HttpResponse(
		json_str,
		content_type="application/json",
	)
	response["Access-Control-Allow-Origin"] = "*"
	return response


def json_response(data, code=200):
	data = {
		"code": code,
		"msg": "success",
		"data": data,
	}
	return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
	data = {
		"code": code,
		"msg": error_string,
		"data": {}
	}
	data.update(kwargs)
	return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


def current() -> Line:
	line = (
		Line()
		.add_xaxis(list(range(10)))
		.add_yaxis(series_name="A相电流", 
				   y_axis=[randrange(0, 100) for _ in range(10)],
				   is_smooth=True,)
		.add_yaxis(series_name="B相电流", 
				   y_axis=[randrange(0, 100) for _ in range(10)],
				   is_smooth=True,)
		.add_yaxis(series_name="C相电流", 
				   y_axis=[randrange(0, 100) for _ in range(10)],
				   is_smooth=True,)
		.set_global_opts(
			title_opts=opts.TitleOpts(title="电流"),
			xaxis_opts=opts.AxisOpts(type_="value"),
			yaxis_opts=opts.AxisOpts(type_="value")
		)
		.dump_options_with_quotes()
	)
	return line

# Create an instance of Chart to get data of chart
voltage_ab_chart = Chart(models.Voltage_AB)

def voltage() -> Line:
	data = voltage_ab_chart.get_data(250)
	line = (
		Line()
		.add_xaxis(list(range(50)))
		.add_yaxis(series_name="", 
				   y_axis=data,
				   is_smooth=True,)
		.set_global_opts(
			title_opts=opts.TitleOpts(title="电压"),
			xaxis_opts=opts.AxisOpts(type_="value"),
			yaxis_opts=opts.AxisOpts(type_="value")
		)
		.dump_options_with_quotes()
	)
	return line

def temperature() -> Line:
	line = (
		Line()
		.add_xaxis(list(range(10)))
		.add_yaxis(series_name="", 
				   y_axis=[randrange(0, 100) for _ in range(10)],
				   is_smooth=True,)
		.set_global_opts(
			title_opts=opts.TitleOpts(title="温度"),
			xaxis_opts=opts.AxisOpts(type_="value"),
			yaxis_opts=opts.AxisOpts(type_="value")
		)
		.dump_options_with_quotes()
	)
	return line


class CurrentChart(APIView):
	def get(self, request, *args, **kwargs):
		return JsonResponse(json.loads(current()))
	
class VoltageChart(APIView):
	def get(self, request, *args, **kwargs):
		return JsonResponse(json.loads(voltage()))

class TemperatureChart(APIView):
	def get(self, request, *args, **kwargs):
		return JsonResponse(json.loads(temperature()))


cnt = 9


class ChartUpdateView(APIView):
	def get(self, request, *args, **kwargs):
		global cnt
		cnt = cnt + 1
		return JsonResponse({"name": cnt, "value": randrange(0, 100)})

class IndexView(APIView):
	def get(self, request, *args, **kwargs):
		# return HttpResponse(content=open("./templates/index.html").read())
		return render(request, 'chart/index.html')

class CurrentView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, 'chart/current.html')

class VoltageView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, 'chart/voltage.html')

class TemperatureView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, 'chart/temperature.html')

def overviewData(request):
	curr_time = models.Temp_rotator.objects.last().create_time
	current_a = str(models.Current_A.objects.last().value)
	current_b = str(models.Current_B.objects.last().value)
	current_c = str(models.Current_C.objects.last().value)
	voltage_ab = str(models.Voltage_AB.objects.last().value)
	voltage_bc = str(models.Voltage_BC.objects.last().value)
	voltage_ca = str(models.Voltage_CA.objects.last().value)
	temp_fore_winding_a = str(models.Temp_fore_winding_A.objects.last().value)
	temp_fore_winding_b = str(models.Temp_fore_winding_B.objects.last().value)
	temp_fore_winding_c = str(models.Temp_fore_winding_C.objects.last().value)
	temp_controller_env = str(models.Temp_controller_env.objects.last().value)
	temp_fore_bearing = str(models.Temp_fore_bearing.objects.last().value)
	temp_rear_bearing = str(models.Temp_rear_bearing.objects.last().value)
	temp_rotator = str(models.Temp_rotator.objects.last().value)
	temp_water = str(models.Temp_water.objects.last().value)
	rev = str(models.Rev.objects.last().value)

	stuff_for_frontend = {
		'create_time': str(curr_time),
		'current_a': current_a + 'A',
		'current_b': current_b + 'A',
		'current_c': current_c + 'A',
		'voltage_ab': voltage_ab + 'V',
		'voltage_bc': voltage_bc + 'V',
		'voltage_ca': voltage_ca + 'V',
		'temp_fore_winding_a': temp_fore_winding_a + '℃',
		'temp_fore_winding_b': temp_fore_winding_b + '℃',
		'temp_fore_winding_c': temp_fore_winding_c + '℃',
		'temp_controller_env': temp_controller_env + '℃',
		'temp_fore_bearing': temp_fore_bearing + '℃',
		'temp_rear_bearing': temp_rear_bearing + '℃',
		'temp_rotator': temp_rotator + '℃',
		'temp_water': temp_water + '℃',
		'rev': rev + 'r/min',
	}

	# return render(request, 'chart/overview.html', stuff_for_frontend)
	return JsonResponse(stuff_for_frontend)

def overview(request):
	return render(request, 'chart/overview.html')
	
