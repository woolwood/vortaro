from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Madde

def query_madde(request, query_term):
    """
    Query a term in the database by headword.
    """
    # query_term = "araba"
    headwords = Madde.objects.filter(madde__startswith=query_term)

    return render(request, 'vortaro/madde.html', {'headwords': headwords})


