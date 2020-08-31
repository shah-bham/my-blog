from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def edit_page(request):
    return render(request, 'edit.html')