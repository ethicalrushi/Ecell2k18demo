from django.shortcuts import render
from .models import Speaker
from django.http import JsonResponse
# Create your views here.

def get_speakers(request):
	speakers = Speaker.objects.all().values()
	speakers_list = list(speakers)
	return JsonResponse(speakers_list, safe=False)
