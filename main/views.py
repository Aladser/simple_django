from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        text = request.POST['text']
        print(f"{email} {text}")

    return render(request, 'main/index.html')
