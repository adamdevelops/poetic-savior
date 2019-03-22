
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Poem

def bloghome(request):
    poems = Poem.objects.all().order_by('date')
    return render(request, 'bloghome.html', {'poems': poems})
