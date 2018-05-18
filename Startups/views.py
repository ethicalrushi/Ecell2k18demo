from django.shortcuts import render
from .models import Startup
from django.http import JsonResponse

def get_startups(request):
	startups = Startup.objects.all().values()
	startups_list = list(startups)
	return JsonResponse(startups_list, safe=False)
