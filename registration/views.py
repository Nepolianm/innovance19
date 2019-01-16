from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def registration(request):
    return render(request,"register.html",{})

def register( request ):
    if request.method != "POST":
        return HttpResponse("Page not found")

    # fetch the data
    # create row in table
    # return acknowldegement page
