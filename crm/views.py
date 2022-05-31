from django.shortcuts import render
from .models import SliderCrm



def first_page(request):
    slider = SliderCrm.objects.all()
    obj_dict = {
        'slider': slider
    }
    return render(request, './index.html', context=obj_dict)
