from django.shortcuts import render
from django.http import HttpResponse

# request -> response
# Request Handler
# Action

# Similar to controller in Express
def say_hello(request):
    return render(request, 'hello.html', {"name": "Yash"})

