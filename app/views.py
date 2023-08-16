from django.shortcuts import render

# Create your views here.

def bs_download(request):
    return render(request,'bs_download.html')