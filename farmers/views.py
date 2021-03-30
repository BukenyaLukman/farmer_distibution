from django.shortcuts import render
from django.http import HttpResponse
import json
import os
import sys
from django.http import JsonResponse
from django.core import serializers





def home_view(request):
	districts = []
	with open('/home/bukenya/Downloads/DjangoApplications/ezy_env/farmer_dist/farmers/interview.json', "r") as interview_dist:
		data = json.load(interview_dist)
		for item in data:
			districts.append({
				"district": item['district'],
				"number": item['number']
			})
			#print(item)
			# for key,value in item.items():
			# 	print(key,value)
	return JsonResponse({"data": districts}, safe=False)
	#return render(request,'index.html', context)



def farmers_view(request):
	context = {}
	return render(request, "farmers/index.html", context)


