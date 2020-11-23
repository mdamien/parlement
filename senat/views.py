from django.shortcuts import render

from .models import Senateur

def senateur(request, slug):
    sen = Senateur.objects.get(slug=slug)
    return render(request, template_name="senateur.html", context={
        'senateur': sen
    })