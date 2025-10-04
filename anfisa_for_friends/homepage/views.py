from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream, Category


def index(request):
    template = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description', 'category__title'
        ).filter(
        Q(is_on_main=True)
        & ~Q(is_published=False)
        # | Q(title__contains='пломбир')
        # & Q(is_published=True)
        )#.order_by('title')[1:4]

    context = {'ice_cream_list': ice_cream_list}
    return render(request, template, context)
