from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_param = request.GET.get('sort', 'name')

    if sort_param == 'min_price':
        sort_param = 'price'
    elif sort_param == 'max_price':
        sort_param = '-price'

    phones = Phone.objects.order_by(sort_param).all()
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_entries = Phone.objects.filter(slug__startswith=slug)
    phone = phone_entries[0]

    context = {
        'phone': phone,
    }
    return render(request, template, context)
