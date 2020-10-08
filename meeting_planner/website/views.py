from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")


def about(request):
    return HttpResponse("Hi, This is Ajay from Aptify!")