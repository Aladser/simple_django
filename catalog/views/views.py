from django.shortcuts import render

from catalog.models.contact import Contact


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
