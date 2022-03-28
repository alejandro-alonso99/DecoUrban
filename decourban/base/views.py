from django.shortcuts import render

def add_file(request):

    return render(request, 'base/add_file.html',{})