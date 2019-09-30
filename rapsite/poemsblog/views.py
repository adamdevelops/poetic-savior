from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Poem
from django.http import HttpResponse

def bloghome(request):
    poems = Poem.objects.all().order_by('date')
    return render(request, 'bloghome.html', {'poems': poems})

def blog_detail(request, pk):
    # print (pk)
    poem = Poem.objects.get(pk=pk)
    # print (poem)
    return render(request, 'blogdetail.html', {'poem': poem})
