from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login3.html')