from django.shortcuts import render, redirect
import requests
from requests_oauthlib import OAuth1

auth = OAuth1("76991a27d3d848e6a1941ee9e9c8d778", "2c03e6c9217b4d31b9315c4763574223")
endpoint = "http://api.thenounproject.com/icon/1"

response = requests.get(endpoint, auth=auth)
print response.content

def espn(request):
    print endpoint
    return render(request,"espn_app/index.html",{"endpoint":endpoint})
