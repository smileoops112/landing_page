from django.shortcuts import render
from .models import PriceCard, PriceTable


def price(request):
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    pt_price = PriceTable.objects.all()
    obj_dict = {
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'pt_price': pt_price,
    }
    return render(request, './index.html', context=obj_dict)