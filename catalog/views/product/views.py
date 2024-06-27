import math

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from catalog.models import Product, Category

PAGINATION_ELEM_COUNT = 5


def index(request):
    page_number = int(request.GET['page']) if 'page' in request.GET else 1
    # начальный диапазон выборки данных из БД
    prd_list_start = (page_number - 1) * PAGINATION_ELEM_COUNT

    products_dict = Product.objects.filter(is_active=True)
    pages_count = math.ceil(len(products_dict) / PAGINATION_ELEM_COUNT)
    pages_list = [i + 1 for i in range(pages_count)] if pages_count > 1 else None

    products_dict = products_dict.order_by('-updated_at').values()[prd_list_start:prd_list_start + PAGINATION_ELEM_COUNT]
    for prd in products_dict:
        prd['category'] = Category.objects.filter(pk=prd['category_id']).get().name
        del prd['category_id']
        prd['name'] = prd['name'][:100]

    return render(request, 'catalog/product/index.html',
                  {
                      'title': 'Склад',
                      'header': 'Список товаров',
                      'products': products_dict,
                      'pages': {
                          'number': page_number,
                          'count': pages_count,
                          'list': pages_list
                      }
                  })


def show(request, pk):
    product = Product.objects.filter(pk=pk).get()
    title = f"Склад - {product.name}"
    return render(
        request,
        'catalog/product/detail.html',
        {'title': title, 'header': product.name, 'product': product}
    )


def create(request):
    return render(
        request,
        'catalog/product/create.html',
        {
            'title': 'Склад - добавление товара',
            'header': 'Добавить товар',
            'categories': Category.objects.all()
        }
    )


def store(request):
    product_dict = {}
    for prd in request.POST.items():
        if prd[0] != 'csrfmiddlewaretoken':
            if prd[0] in ('category_id', 'price'):
                product_dict[prd[0]] = int(prd[1])
            else:
                product_dict[prd[0]] = prd[1] if prd[1] != '' else None

    Product.objects.create(**product_dict)
    return HttpResponseRedirect('/')