from django.shortcuts import render
from django.http import HttpResponse
from .models import Sample,Skill,Language,Image,Overview,Framework,Target

def home(request):
    skills=Skill.objects.all()
    return  render(request,'index.html',{"skills":skills})

def projects(request):
    return  HttpResponse("these are my projects")

def screenshots(request):
    return HttpResponse('screenshots')
