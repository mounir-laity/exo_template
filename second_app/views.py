from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, "second_app/hello.html")

def index(request):
    return render(request, "second_app/index.html")