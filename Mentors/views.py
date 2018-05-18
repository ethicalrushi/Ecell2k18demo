from django.shortcuts import render
from .models import Mentor
from django.http import JsonResponse

def get_mentors(request):
    mentors=Mentor.object.all().values()
    mentors_list=list(mentors)

    return JsonResponse(mentors_list, safe=False)
