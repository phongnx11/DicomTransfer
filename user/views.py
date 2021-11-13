from django.shortcuts import render

# Create your views here.

def dicom(request):
    return render(request,"dicom.html")