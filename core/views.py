import random
from datetime import date

from django.shortcuts import render

from senat.models import Senateur

def home(request):
    senateurs = list(Senateur.objects.all())
    random.seed(str(date.today()))
    senateur = random.choice(senateurs)

    return render(request, template_name='home.html', context={
        'senateur': senateur,
    })