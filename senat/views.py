from django.shortcuts import render

def senateur(request):
    return render(request, template_name="senateur.html")