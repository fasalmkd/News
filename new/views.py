from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    response = requests.get('https://saurav.tech/NewsAPI/everything/cnn.json')
    posts = response.json()
    data = posts['articles']
    return render(request,"index.html",{'post':data})
# Create your views here.
