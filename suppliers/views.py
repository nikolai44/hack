from django.shortcuts import render
from .forms import FactureForm
import json
from django.http import JsonResponse
from .models import FactureModel
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


def home_view(request):
    return render(request,
                  'home.html')


def get_id(request, uid):
    facture = FactureModel.objects.get(pk=uid)

    return render(request,
                  'jason.html',
                    {'facture': facture})


def add_facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            facture = form.save()
            return JsonResponse({'uid': facture.id})
    else:
        form = FactureForm()
    return render(request,
                  'facture.html',
                  {
                      'form': form
                  })
