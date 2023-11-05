from django.shortcuts import render,HttpResponse

# Create your views here.

def profile(request):
    return HttpResponse('<h1> This is Student profile page </h1>')
def bi (request):
    return HttpResponse('<h1> This is student book issued page</h1>')
