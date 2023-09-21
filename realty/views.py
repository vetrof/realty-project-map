from django.shortcuts import render

from realty.models import Realty

from tbot.parser.parser import parsing

# parsing()


def index_views(request):
    return render(request, 'index.html')


def detail_views(request, id):
    realty = Realty.objects.get(id=id)
    return render(request, 'detail.html', {'realty': realty})
