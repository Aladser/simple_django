from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(f"Пользователь {name}({phone}) написал: {message}")

    return render(request, 'catalog/contacts.html')
