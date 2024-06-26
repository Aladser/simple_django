from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from catalog.models import Product, Contact, Category


def index(request):
    products = Product.objects.all().order_by('-updated_at').values()
    for prd in products:
        prd['category'] = Category.objects.filter(pk=prd['category_id']).get().name
        del prd['category_id']
        prd['name'] = prd['name'][:100]

    return render(request, 'catalog/product/index.html',
                  {'title': 'Склад', 'header': 'Список товаров', 'products': products})


def product_show(request, pk):
    product = Product.objects.filter(pk=pk).get()
    title = f"Склад - {product.name}"
    return render(
        request,
        'catalog/product/detail.html',
        {'title': title, 'header': product.name, 'product': product}
    )


def product_create(request):
    return render(
        request,
        'catalog/product/create.html',
        {
            'title': 'Склад - добавление товара',
            'header': 'Добавить товар',
            'categories': Category.objects.all()
        }
    )


def product_store(request):
    product_dict = {}
    for prd in request.POST.items():
        if prd[0] != 'csrfmiddlewaretoken':
            product_dict[prd[0]] = prd[1] if prd[1] != '' else None

    Product.objects.create(**product_dict)
    return HttpResponseRedirect("/")


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(f"Пользователь {name}({phone}) написал: {message}")

    return render(
        request,
        'catalog/contacts.html',
        {'title': 'Склад - контакты', 'header': 'Контакты', 'contacts': Contact.objects.all()}
    )
