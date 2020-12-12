from django.shortcuts import render

from django.http import HttpResponse
 
def home(request):
    return render(request, "home.html", {
        "name": "Yash",
        "age":"18",
        "height":"176 cm"
    })




