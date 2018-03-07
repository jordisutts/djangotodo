from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


# Create your views here.
def get_index(request):
	return render(request,"comments/index.html")