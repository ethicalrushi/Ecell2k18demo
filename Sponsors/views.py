from django.shortcuts import render
from .models import Sponsor
from django.http import JsonResponse

# Create your views here.

def get_sponsors(request):
	sponsors = Sponsor.objects.all().values('name','details','contact','pic','website','spons_type')
	sponsors_list = list(sponsors)
	return JsonResponse(sponsors_list, safe=False)