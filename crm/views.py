from django.shortcuts import render
from .models import SliderCrm
from cms.forms import OrderForm
from cms.models import Order
from price.models import PriceCard, PriceTable
from telebot.send_message import sendTelegram


def first_page(request):
    slider = SliderCrm.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    pt_price = PriceTable.objects.all()
    form = OrderForm()
    obj_dict = {
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'pt_price': pt_price,
        'slider': slider,
        'form': form,
    }
    return render(request, './index.html', context=obj_dict)


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    sendTelegram(tg_name=name, tg_phone=phone)
    obj_dict = {
        'name': name,
        'phone': phone,
        'element': element
    }
    return render(request, './thanks.html', context={'name': name, })
