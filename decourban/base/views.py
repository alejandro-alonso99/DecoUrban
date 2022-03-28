from xml.dom.minidom import Document
from django.shortcuts import redirect, render

def add_file(request):
    if request.method == 'POST':

        updated_file = request.FILES['document']
        print(updated_file.name)
        print(updated_file.size)
    
    return render(request, 'base/add_file.html',{})