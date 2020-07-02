import json
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Line
from pyecharts import options as opts

from django.shortcuts import render

# Create your views here.
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

def voltage() -> Line:
    line = (
        Line()
        .add_xaxis(list(range(10)))
        .add_yaxis(series_name="", 
				   y_axis=[randrange(0, 100) for _ in range(10)],
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