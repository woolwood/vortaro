from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q
from .models import Madde

def get_madde(request, query_term):
    """
    Look up a headword by exact match.
    """
    headwords = Madde.objects.filter(madde__iexact=query_term).prefetch_related("anlam_set")
    return render(request, 'vortaro/madde.html', {'headwords': headwords})

# def query_madde(request, query_term):
#     """
#     Query a term in the database by headword.
#     """
#     # query_term = "araba"
#     headwords = Madde.objects.filter(madde__startswith=query_term).prefetch_related("anlam_set")
#
#     return render(request, 'vortaro/madde.html', {'headwords': headwords})


def index(request):
    return render(request, 'vortaro/index.html')

def search_index(request):
    query_term = request.GET.get('search')
    headwords = Madde.objects.filter(madde__icontains=query_term).prefetch_related("anlam_set")
    return render(request, 'vortaro/search_results.html', {'headwords': headwords})

