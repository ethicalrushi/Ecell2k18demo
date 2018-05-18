from django.shortcuts import render
from .models import App
from django.http import JsonResponse

def get_app(request):
	app_ver = app.objects.all().values()
	app_ver_list = list(app_ver)
	return JsonResponse(app_ver_list, safe=False)
