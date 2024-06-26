from django.shortcuts import render
from catalog.models import Product, Contact, Category


def index(request):
    products = Product.objects.all().order_by('-updated_at').values()
    for prd in products:
        prd['category'] = Category.objects.filter(pk=prd['category_id']).get().name
        del prd['category_id']
        prd['name'] = prd['name'][:100]

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
