from django.shortcuts import render
from catalog.models import Product


def index(request):
    products = Product.objects.all().order_by('-updated_at').values()[:5]
    [print(el) for el in products]

    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(f"Пользователь {name}({phone}) написал: {message}")

    return render(request, 'catalog/contacts.html')
