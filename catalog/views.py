from django.shortcuts import render
from catalog.models import Product, Contact


def index(request):
    products = Product.objects.all().order_by('-updated_at').values()[:5]

    return render(request, 'catalog/product/index.html', {'products': products})


def product_show(request, pk):
    return render(
        request,
        'catalog/product/detail.html',
        {'product': Product.objects.filter(pk=pk).get()}
    )


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(f"Пользователь {name}({phone}) написал: {message}")

    return render(request, 'catalog/contacts.html', {'contacts': Contact.objects.all()})
