from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
# from django.utils import timezone
# from django.db.models import Q
from django.db.models.functions import Lower
from .models import Madde
import itertools


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
    query_term = request.GET.get('search')

    # Use itertools.chain() to concatenate three separate queries,
    # preserving the pre-sorted order in the final queryset.
    # Allows us to display most relevant matches first.
    if query_term:
        exact_query = (Madde.objects.filter(madde__iexact=query_term)
                       .order_by('madde')
                       .prefetch_related("anlam_set"))
        startswith_query = (Madde.objects.filter(madde__istartswith=query_term)
                            .exclude(pk__in=exact_query)
                            .order_by(Lower('madde').asc())
                            .prefetch_related("anlam_set"))
        contains_query = (Madde.objects.filter(madde__icontains=query_term)
                          .exclude(pk__in=exact_query)
                          .exclude(pk__in=startswith_query)
                          .order_by(Lower('madde').asc())
                          .prefetch_related("anlam_set"))
        headwords = itertools.chain(exact_query, startswith_query, contains_query)
        return render(request, 'vortaro/index.html', {'headwords': headwords})
    else:
        return render(request, 'vortaro/index.html')
