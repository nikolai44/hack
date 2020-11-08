from django.shortcuts import render
from .forms import FactureForm
import json
import os
from django.http import JsonResponse
from .models import FactureModel
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import qrcode
from django.shortcuts import redirect

fullpath = os.path.abspath(__file__)
absdir = os.path.dirname(fullpath)

def home_view(request):
    return render(request,
                  'home.html')

def add_geodata(request):
    return render(request,
                  'home.html')

def get_id(request, uid):
    facture = FactureModel.objects.get(pk=uid)

    return render(request,
                  'mobile.html',
                  {'facture': facture})

def add_facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            facture = form.save()
            data = "http://18.134.250.128:8000/get_info/" + str(facture.id)
            filepath = os.path.join(absdir, "../qr/qr" + str(facture.id) + ".png")
            img = qrcode.make(data)
            img.save(filepath)
            response = redirect("../qr/qr" + str(facture.id) + ".png")
            return response
    else:
        form = FactureForm()
    return render(request,
                  'facture.html',
                  {
                      'form': form
                  })
