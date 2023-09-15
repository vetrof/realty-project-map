from django.shortcuts import render

from realty.models import Realty


def detail_views(request, id):
    realty = Realty.objects.get(id=id)
    return render(request, 'detail.html', {'realty': realty})
